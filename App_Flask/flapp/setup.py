from setuptools import find_packages, setup

setup(
    name='flapp',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)


class Inputform(FlaskForm):
    timeline = StringField('timeline', validators=[DataRequired()])
    blue_destr_tower = IntegerField('blue_destr_tower', validators=[DataRequired()])
    blue_gold = IntegerField('blue_gold', validators=[DataRequired()])
    red_destr_tower = IntegerField('red_destr_tower', validators=[DataRequired()])
    red_gold = IntegerField('red_gold', validators=[DataRequired()])
    k_d_a_1 = StringField('kda1', validators=[DataRequired()])
    k_d_a_2 = StringField('kda2', validators=[DataRequired()])
    k_d_a_3 = StringField('kda3', validators=[DataRequired()])
    k_d_a_4 = StringField('kda4', validators=[DataRequired()])
    k_d_a_5 = StringField('kda5', validators=[DataRequired()])
    k_d_a_6 = StringField('kda6', validators=[DataRequired()])
    k_d_a_7 = StringField('kda7', validators=[DataRequired()])
    k_d_a_8 = StringField('kda8', validators=[DataRequired()])
    k_d_a_9 = StringField('kda9', validators=[DataRequired()])
    k_d_a_10 = StringField('kda10', validators=[DataRequired()])
    submit = SubmitField('soumettre les valeurs')