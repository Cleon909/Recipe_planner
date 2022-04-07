class AddRecipeForm(FlakForm):
    name = StringField('Name of Recipe', validators = [DataRequired(), Length(max = 200)])
    