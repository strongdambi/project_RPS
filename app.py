from flask import Flask, render_template, request
import random
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#  가독성을 위해 db 위치 이동


class GameResult(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    com = db.Column(db.String, nullable=False)
    user = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    user_choice = ""
    com_choice = ""
    result = ""

    if request.method == 'POST':
        user_choice = request.form['user_choice']  # 선택한 값(클릭)을 form 데이터에서 가져옴
        result, com_choice = game(user_choice)

    results = GameResult.query.all()

    # 승무패 카운트
    wins = GameResult.query.filter_by(result='승').count()
    draws = GameResult.query.filter_by(result='무').count()
    losses = GameResult.query.filter_by(result='패').count()

    return render_template('index.html', results=results, wins=wins, draws=draws, losses=losses, user_choice=user_choice, com_choice=com_choice, result=result)


def game(user):
    # 가위바위보
    select = ["가위", "바위", "보"]
    com = random.choice(select)

# 컴퓨터와 유저가 같은 선택 시
    if com == user:
        result = "무"
# 유저가 이기는 경우
    elif (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"):
        result = "승"
# 그외 = 컴퓨터가 이기는 경우
    else:
        result = "패"

# 결과를 입력할 인덱스 결정
    with app.app_context():
        max_index = db.session.query(db.func.max(GameResult.index)).scalar()
        if max_index is None:
            max_index = 0  # 0으로 수정
        new_index = max_index + 1

# 지정 인덱스로 결과 입력
        new_game_result = GameResult(
            index=new_index, com=com, user=user, result=result)
        db.session.add(new_game_result)
        db.session.commit()

    return result, com


if __name__ == "__main__":
    app.run()
