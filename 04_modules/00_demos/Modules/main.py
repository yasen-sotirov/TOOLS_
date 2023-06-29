# Option 1: import module 'object' - all functions are available
import text

# Option 2: import only what you need
from shapes import rectangle_area

# for nested modules: folder_name.module_name
from data.courses import check_for_course

# When option 1 is used: Module functions are accessed by typing module_name.function_name
print(text.camel_case(['One', 'large', 'burger', 'please']))
print(text.kebab_case(['One', 'large', 'burger', 'please']))

# When option 2 is used: use imported function directly
print(rectangle_area(2, 3))
print(check_for_course('Fundamentals'))

# circle_area() is not available
# shapes.circle_area() is also not available
