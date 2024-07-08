import validation
import glob
import query_generator
field = validation.BattlefieldValidation("output/20_units/generated_plan_1.json")
output = field.get_model_output()
input = field.get_initial_positions()
field.check_metadata()
print(field.p_id, field.p_type, field.p_alliance, field.p_pos)
print(field.get_tasks())
field.check_movement()
print(field.movement_check_arr)