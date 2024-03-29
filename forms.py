from itertools import product
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, SelectField, TextAreaField, FloatField, RadioField, FormField
from wtforms.validators import DataRequired, NumberRange


class CreateTF(FlaskForm):
    # 題目內容
    content = TextAreaField('題目內容', validators=[DataRequired()])

    True_or_False = RadioField('正確答案', choices=[
        ('T', '正確'), ('F', '錯誤')], validators=[DataRequired()])


class CreateMC(FlaskForm):
    # 題目內容
    content = TextAreaField('題目內容', validators=[DataRequired()])

    # 選項A
    A = TextAreaField('A', validators=[DataRequired()])

    # 選項B
    B = TextAreaField('B', validators=[DataRequired()])

    # 選項C
    C = TextAreaField('C', validators=[DataRequired()])

    # 選項B
    D = TextAreaField('D', validators=[DataRequired()])

    Which_True = RadioField('正確答案', choices=[
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], validators=[DataRequired()])


class CreateSA(FlaskForm):
    # 題目內容
    content = TextAreaField('題目內容', validators=[DataRequired()])
    # 題目內容
    answer_box = TextAreaField('正確答案', validators=[DataRequired()])


class delete_quiz(FlaskForm):
    # 確認刪除
    confirm = BooleanField('確認是否移除?', validators=[DataRequired()])
    # 送出按鈕
    submit = SubmitField('移除試卷')


class export_quiz(FlaskForm):
    submit = SubmitField('匯出試題')
