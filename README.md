# final-exam
- From the starting code, polygon_art.py, you are to write an OO program that generates different pieces of art works
- Fork, then, clone this repo
- Read the instructions given in the course's Google Classroom and start coding
- Once you are done, push your final code to your Github repo and modify this README to report on the work you have done

# How to run the program
- Click run button or type command <python3 polygon_art.py> in command prompt
- Then program will prompt to input a number 1 - 8 (Inclusive) choose and wait for the result.

# Report

## What I've done in this work

- Implement Canvas class and Polygon class
- Polygon class has attribute that refer to shape information (ex: number of side, size, border_size)
- Polygon class has 2 method (exclude init)
    - draw:  With this method program will draw a shape according to it own attribute but if level is more then one program will draw a smaller shape inside bigger shape by iterate by the number of level. After drawing a shape program will call reduction method to ready for draw a new shape inside.
    - reduction: This method will bring turtle to the new location that compute from reduction ratio and location before then set new location to location attribute. After finish work with location program will multiply size by reduction ratio and set it as a new size attribute.
- Canva class will set up canvas for making art and prompt user for choice. It's attribute will refer to art detail like number of polygon level and random outlined for number of side.
- Canva class has 3 method (exclude init)
    - setting_art: This method will set information for art refer to user choice.
    - making_art: This method will create new polygon object with random information and draw it to make an art.
    - get_new_color: This method will return a random color.