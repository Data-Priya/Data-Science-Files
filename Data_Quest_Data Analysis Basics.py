'''
Python Data Analysis Basics
1 of 10 · Reading the MoMA Dataset
Learn
In this lesson, we'll be analyzing data from the Museum of Modern Art (MoMA) dataset. Here are a few takeaways you can expect by the end of the lesson:

Basic data analysis techniques
How to summarize numeric data
How to format strings in Python
These techniques will be extremely valuable on your path to becoming a data expert. You'll not only use them whenever you analyze data but also when you explore data before performing a more complex task, such as machine learning.

Working with the dataset, we'll learn how to do the following:

Calculate the artist's age when they created their artwork
Analyze and interpret the distribution of artist ages
Create functions that summarize our data
Print summaries in an easy-to-read-way
So that you don't have to clean the data, we have prepared a CSV containing all of the data cleaning necessary: artworks_clean.csv.

Even though we have cleaned the data, we have to convert these values to numeric types so we can analyze them. Some of the rows have missing values, so we'll need to handle those as well.

The code below shows how we would convert only the BeginDate column:

Converting to integer type
We provided code to read in the dataset, and we used this technique to convert both the birth and death date to numeric types. Let's use the technique to also convert the date column.

Instructions
Use a for loop to iterate over each row in the moma list of lists. Inside the body of the loop, do the following:

Assign the value from index 6 (Date) to a variable called date.
Use an if statement to check if date is not equal to "".
If date isn't equal to "", convert it to an integer type using the int() function.
Finally, assign the value back to index 6 in the row.
'''

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for i in moma:
    date = i[6]
    if date != "":
        date = int(date)
    i[6] = date
    
    
'''
Python Data Analysis Basics
2 of 10 · Calculating Artist Ages
Learn
On the next few screens, we're going to work on calculating the ages at which artists created their works of art. We need to subtract the artist's birth year (BeginDate) from the year when they created their artwork (Date).

While every row has a value for Date, there are some that are missing values for BeginDate. When we cleaned BeginDate, we encountered some missing values and left them as empty strings (""). We'll use a value of 0 for these cases, which we'll replace with something more meaningful later.

The flow diagram below illustrates the logic that you'll need to use in your code:

Converting to integer type
There are a few cases when the artist's age (according to our data set) is very low, including some where the age is negative. We could investigate these specific cases one by one, but since we're looking for a summary, we'll take care of these by categorizing artists younger than 20 as "Unknown". This has the handy effect of also categorizing the artists without birth years as "Unknown".

This flow diagram demonstrates the logic to perform this second step:

Converting to integer type
To help you understand some of the values you'll be working with and how they will progress through your code, we've prepared the following table with a sample of data:

Year Artwork Created (date)	Birth Year (birth)	age	final_age
1968	1898	70	70
1931	""	0	"Unknown"
1972	1976	-4	"Unknown"
Now it's time to calculate the ages! Each of the operations in both flow diagrams will require separate code sections. We've provided instructions below to help guide you as you implement the logic.

Instructions
Create an empty list, ages, to store the artist age data.
Use a loop to iterate over the rows in moma.
In each iteration, assign the artwork year (at index 6) to date and artist birth year (at index 3) to birth.
If the birth date is an int, calculate the age of the artist at the time of creating the artwork, and assign it to the variable age.
If birth isn't an int type, assign 0 to the variable age.
Append age to the ages list.
Create an empty list final_ages, to store the final age data.
Use a loop to iterate over each age in ages. In each iteration, do the following:
If the age is greater than 20, assign the age to the variable final_age.
If the age is not greater than 20, assign "Unknown" to the variable final_age.
Append final_age to the final_ages list.
'''

ages = []
for i in moma:
    date = i[6]
    birth = i[3]
    if birth != "":
        age = date-birth
    else:
        age = 0
    ages.append(age)
    
final_ages = []

for age in ages:
    if age >20:
        final_age = age 
    else:
        final_age = "Unknown"
    final_ages.append(final_age)
    
'''
Python Data Analysis Basics
3 of 10 · Converting Ages to Decades
Learn
We now have a list — ages — containing the artist ages when they created their artwork. Because there are many unique ages, we'll calculate only the decade during which the artist created each work. For instance, if we calculate that the artist was 24, we'll record that as the artist being in their "20s."

As a first step toward this, we'll need to remove the last digit in every age:

24 will become 2
86 will become 8
50 will become 5
106 will become 10
Python stores strings in a list-like structure, which lets us slice them in the same way we would a list.

Let's look at a simple example:

Indexing a string
In order to use this technique with our ages, we'll need to do the following:

Convert the integer value to a string.
Use slicing to slice all but the last character.
Removing the last digit from an age
Let's look at that in code form, starting with the original integer value:

age = 24

Explain

Copy
Next, we'll convert the integer to a string, "24":

decade = str(age)

Explain

Copy
We'll slice all but the last character, leaving "2":

decade = decade[:-1]
print(decade)

Explain

Copy
2

Explain

Copy
The final step is to add the substring "0s" to the end of each string:

2 will become 20s
8 will become 80s
5 will become 50s
10 will become 100s
We can use the + operator to join two strings:

combined = "lengthen" + "ing"
print(combined)

Explain

Copy
lengthening

Explain

Copy
For our decade values, this is how it will look:

decade = decade + "0s"
print(decade)

Explain

Copy
20s

Explain

Copy
Let's take our final_ages list, loop over it, and perform the operation above to convert it into a list of decades.

Instructions
Create an empty list, decades, to store the artist decade data.
Iterate over the values in final_ages, and in each iteration, do the following:
If age is "Unknown", assign it to the variable decade
If age isn't "Unknown", do the following:
Convert the integer value to a string and assign it to the variable decade.
Use list slicing to remove the final character of decade.
Use the + operator to add the substring "0s" to the end of the string decade.
Append decade to the decades list.
'''
# The final_ages variable is available
# from the previous screen
decades = []
for i in final_ages:
    if i is "Unknown":
        decade = i
    else:
        decade = str(i)
        decade = decade[:-1]
        decade = decade + "0s"
        
    decades.append(decade)
    
'''
Python Data Analysis Basics
4 of 10 · Summarizing the Decade Data
Learn
On the previous two screens, we did the following:

Calculated the age of the artists when they created their artwork.
Simplified those ages to a list of "decades" so there were fewer unique values.
The final step in our analysis is to count the instances of each decade. To do this, we're going to use a Python fundamentals technique: constructing a frequency table.

A frequency table lists how many of each item there are in a collection of items. We'll recap how this works using a simple example. Let's say we have a list of different types of fruit:

A list of fruit
A frequency table shows us how many of each item we have on our list:

The frequency table of our list
In Python, we commonly store this as a dictionary. We are going to build a dictionary where the keys are the different pieces of fruit, and the values are the number of each fruit in our list. Let's look at a code representation of our list of fruit:

fruit = ['orange', 'orange', 'orange', 'banana',
         'apple', 'banana', 'orange', 'banana',
         'apple', 'banana']

Explain

Copy
Once we have constructed our frequency table as a dictionary, it will look like this:

{
    'orange': 4,
    'banana': 4,
    'apple': 2
}

Explain

Copy
The logical steps we'll need to follow are in the diagram below:

The logic to create a frequency table of our list of fruit
Let's look at how we implement that in code — and how that code looks as we run through each iteration of our loop:

fruit_frequency = {}
​
for f in fruit:
    if f not in fruit_frequency:
        fruit_frequency[f] = 1
    else:
        fruit_frequency[f] += 1
    print(fruit_frequency)

Explain

Copy
{'orange': 1}
{'orange': 2}
{'orange': 3}
{'orange': 3, 'banana': 1}
{'orange': 3, 'banana': 1, 'apple': 1}
{'orange': 3, 'banana': 2, 'apple': 1}
{'orange': 4, 'banana': 2, 'apple': 1}
{'orange': 4, 'banana': 3, 'apple': 1}
{'orange': 4, 'banana': 3, 'apple': 2}
{'orange': 4, 'banana': 4, 'apple': 2}

Explain

Copy
Now that we've covered creating frequency tables, let's use that technique to count the frequencies of the different decades of artist ages. As a reminder, below is an excerpt of the data in our ages list:

[47, 55, 51, 36, 'Unknown', 52]

Explain

Copy
Instructions
Create an empty dictionary, decade_frequency.
Iterate through each item in the decades list. In each iteration, do the following:
If the item is not a key in decade_frequency, add it as a key with a value of 1.
If the item is a key in decade_frequency, add one to the existing value for that key.
'''

# The decades variable is available
# from the previous screen

decade_frequency = {}

for i in decades:
    if i not in decade_frequency:
        decade_frequency[i] = 1
    else:
        decade_frequency[i] += 1
        
print(decade_frequency) #{'30s': 4722, '60s': 1357, '70s': 559, '40s': 4081, '50s': 2434, '20s': 1856, 'Unknown': 1093, '90s': 253, '80s': 364, '100s': 3, '110s': 3}

'''
Python Data Analysis Basics
5 of 10 · Inserting Variables into Strings
Learn
Most of what we've learned so far has been about cleaning and interpreting data stored in string form.

Another common application of strings is displaying output in an easy-to-read form. One example would be if we wanted to insert a list of values into a sentence. Let's say we have some data about one of our friend's favorite numbers:

name = "Kylie"
num = 8

Explain

Copy
And we wanted to print output like the following:

Kylie's favorite number is 8

Explain

Copy
Using what we know, we could use the + operator to combine the values, using str() to convert the integer:

output = name + "'s favorite number is " + str(num)
print(output)

Explain

Copy
Kylie's favorite number is 8

Explain

Copy
As you can see, this requires a lot of work for what seems like a simple task! Luckily, there is a much easier way.

The str.format() method is a powerful tool that helps us write easy-to-read code while combining strings with other variables.

There are also extra things that str.format() can do with formatting numbers, but for now we'll focus on inserting values into strings.

We use the method with a string — which acts as a template — using the brace characters ({}) to signify where we want to insert any variables. We then pass those variables as arguments to the method. Let's look at a few examples:

output = "{}'s favorite number is {}".format("Kylie", 8)
print(output)

Explain

Copy
Kylie's favorite number is 8

Explain

Copy
As you can see, our code is very easy to understand, and str.format() converts the integer to a string. The variables are inserted into the {} in the order we pass them as arguments.

If we want to specify ordering and/or repeat numbers, we can use integers:

output = "{0}'s favorite number is {1}, {1} is {0}'s favorite number".format("Kylie", 8)
print(output)

Explain

Copy
Kylie's favorite number is 8, 8 is Kylie's favorite number

Explain

Copy
Lastly, if we want to make things clearer, we can give each variable a name — technically this is using keyword arguments.

When we use keyword arguments to pass values to str.format(), we can use those names inside our braces. Because our string is becoming long, we're going to create a separate template string, and call the str.format() directly on it:

template = "{name}'s favorite number is {num}, {num} is {name}'s favorite number"
output = template.format(name="Kylie", num="8")
print(output)

Explain

Copy
Kylie's favorite number is 8, 8 is Kylie's favorite number

Explain

Copy
Choosing which way to use str.format() is largely a matter of taste, but we recommend thinking about readability. If what you're doing is complex, using numbers or names inside the braces definitely makes things easier!

In the exercise below, your job will be to insert an artist's name and birth year into a formatted string. As an example, for the artist René Magritte, the format would be as follows:

René Magritte's birth year is 1898

Explain

Copy
Instructions
We have provided an artist's name and birth year in the artist and birth_year variables.

Create a template string to insert the artist and birth_year variables into a string using the format provided above. You may use your choice of the three techniques you learned for specifying which variables go where.
Use str.format() to insert the two variables into your template string; assign the result to a variable.
Use the print() function to call that variable.
'''

artist = "Pablo Picasso"
birth_year = 1881
template = "{name}'s birth year is {year}"

output = template.format(name = artist, year = birth_year)

print(output)

'''

Python Data Analysis Basics
6 of 10 · Creating an Artist Frequency Table
Learn
On the next screen, we're going to create a function that will print some summary information about an artist. Before we do, we're going to prepare the underlying data by creating a frequency table that counts how many works of art are in our dataset for each artist.

We can use the same technique we used to create our earlier frequency table with one minor modification — we will be iterating over a list of lists instead of a simple list that we used to create our decades frequency table.

The only difference this makes is that we will first need to extract the value we want to count from the row before we start. As an example, we'll look at the code required to make a frequency table of the different genders in our dataset.

The code block below might look intimidating at first glance, but everything in it is a concept you've seen before. We've added comments so you can follow along with the logic.

The code to create a gender frequency table
Let's use that technique to make the frequency table of how many works of art each artist has in our MoMA dataset.

Instructions
Create an empty dictionary, artist_freq.
Iterate through each item in the moma list of lists. In each iteration, do the following:
Assign the artist's name (column index 1) to the variable artist.
If artist is not a key in artist_freq, add it as a key with a value of 1.
If artist is a key in artist_freq, add one to the existing value for that key.
'''

artist_freq = {}

for i in moma:
    artist = i[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1
        
print(artist_freq)

'''
ython Data Analysis Basics
7 of 10 · Creating an Artist Summary Function
Learn
Now that we've created a dictionary containing the counts of each artist's works of art in our dataset, the final part of our task will be creating a function that displays information for a specific artist.

Our function will take a single argument — the name of an artist — and display a formatted sentence about that artist. The diagram below illustrates the input and output.

Artist summary logic
Inside the function, we'll need to do the following:

Retrieve the number of works of art by the artist from the artist_freq dictionary
Define a template for our output
Use str.format() to insert the artists name and number of works of art into our template
Use the print() function to display the output
The artist_freq dictionary you made in the previous screen will be available to you.

Instructions
Create a function artist_summary() that accepts a single argument: the name of an artist.
The function should print a summary of the artist using the steps below:
Retrieve the number of works of art from the artist_freq dictionary, and assign it to a variable.
Create a template string that uses braces ({}) to insert the name and variables into the string, using the format from the diagram above.
Use str.format() method to insert the artist's name and number of works of art into the string template.
Use the print() function to display the final string.
Use your function to display a summary for the Artist "Henri Matisse".
'''

def artist_summary(artist_name):
    if artist_name  in artist_freq:
        num_artworks = artist_freq[artist_name]
        template = "There are {num} artworks by {name} in the dataset"
        artist_name = template.format(num = num_artworks, name = artist_name)
    return artist_name
                

print(artist_summary("Henri Matisse"))

'''
Python Data Analysis Basics
8 of 10 · Formatting Numbers Inside Strings
Learn
On the previous screens, we learned how to insert variables into strings using the str.format() method. Another powerful use of the method is helping us apply formatting to numbers as they are inserted into the string. This can make our data more readable, especially in the case of long decimal numbers. Let's look at a quick example:

num = 32.554865
print("I own {pct}% of the company".format(pct=num))

Explain

Copy
I own 32.554865% of the company

Explain

Copy
For most cases, having six numbers after the decimal point — also called precision — is unnecessary. One approach might be that instead of a precision of 6, we only want to show a precision of 2:

I own 32.55% of the company

Explain

Copy
We specify number formatting, including things like precision, by adding one of various format specifications inside the braces ({}) of our string. There are many different parts to this format specification part of the documentation, but because the complexity makes it difficult to understand, we're going to just focus on the most common ones you'll need.

To indicate the precision of two, we specify :.2f after the name or position of our argument:

Specifying precision
If you are not specifying a named/positional argument, you just leave that part out:

Specifying precision
Another useful format specification is to add a comma as a thousands separator, which prevents large numbers from being hard to read, as in the example below:

print("The approximate population of {0} is {1}".format("India",1324000000))

Explain

Copy
The approximate population of India is 1324000000

Explain

Copy
To add a comma, you would use the syntax :, inside the brackets, after the number or name of the variable you're inserting:

Specifying the comma separator
The output of this code is below:

The approximate population of India is 1,324,000,000

Explain

Copy
As you can see, this is much easier to read! We can also combine the thousands separator and the precision by specifying them in this order:

Specifying precision and the comma separator
The output of this code is below:

Your bank balance is $12,345.68

Explain

Copy
Note that a specific order is necessary – If we don't follow this order, our code will return a ValueError:

The name or position of the variable
A colon (:) to start the format spec
The thousands separator
The precision
The easy way to remember this order is that in a number like 3,412.69, the comma comes before the decimal point in the same way the thousands separator comes before the precision.

We'll use this technique on some MoMA data on the next screen, but for now we'll keep things simple and practice using some data on world populations. For each country, you'll need to display data that conforms to the following format:

The population of China is 1,379.30 million

Explain

Copy
Instructions
Create a template string that will insert the country name and population as shown in the example above.
The country population should have a precision of two and use a comma separator.
Use a for loop to iterate over the pop_millions list of lists and in each iteration, do the following:
Assign the country name and population to two variables.
Use str.format() to insert the two variables into your template string.
Use the print() function to display the result of your str.format() call.
'''

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for item in pop_millions:
    country_name = item[0]
    country_population = item[1]
   
    template = "The population of {name} is {population:,.2f} million"
    tem_str = template.format(name=country_name, population=country_population)
    
    print(tem_str)
    

'''
Python Data Analysis Basics
9 of 10 · Challenge: Summarizing Artwork Gender Data
Learn
The final exercise for this lesson will combine two techniques to analyze and display information about the frequencies of artwork by artists of different genders. The two techniques we'll combine are as follows:

Creating a frequency table of the genders in the dataset, which we have done for both the artists' ages and the artists themselves
Using the str.format() and the str formatting specification to display the data in an easy-to-read format, which we've done on both of the previous two screens
One technique you'll need to use that we haven't learned yet is looping over a dictionary, which you'll need to use to display the data in the frequency table that you make.

We'll work with the fruits_freq frequency table we created earlier in this lesson.

print(fruit_freq)

Explain

Copy
{
    'orange': 4,
    'banana': 4,
    'apple': 2
}

Explain

Copy
We use the dict.items() method, which returns each of the key-value pairs from our dictionary one-at-a-time. This helps us loop over dictionaries more easily. We can assign both the key and value (in that order) when we define our loop:

for fruit, qty in fruit_freq.items():
    output = "I have {q} {f}s".format(f=fruit, q=qty)
    print(output)

Explain

Copy
I have 4 oranges
I have 4 bananas
I have 2 apples

Explain

Copy
This screen is a challenge screen, which means we'll provide you with less specific instructions than on a regular screen. You might find that this takes you a few more attempts than it normally would, but that's okay!

This screen will help you experience a real-life data analysis workflow — you'll write some code, run it, and if it doesn't work, you'll have to troubleshoot before moving on to the next part.

We've provided some extra hints, plus you can click "Back" to look at earlier screens if you need to revise any concepts. Before we begin, let's quickly recap our task:

You'll create a frequency table dictionary containing counts of the values in the Gender column.
You'll loop over the dictionary, and use str.format() to print a formatted line of output summarizing each key-value pair in the dictionary. The format of the output will be as follows:
There are 2,443 artworks by Female artists

Explain

Copy
Instructions
Create a frequency table for the values in the Gender (row index 5) column.
Loop over each key-value pair in the dictionary. Display a line of output in the format shown above summarizing each pair.
'''


gender_freq = {}

for i in moma:
    gender = i[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1
        
print(gender_freq)

for gender, qty in gender_freq.items():
    output = "There are {q:,} artworks by {g} artists".format(g=gender, q=qty)
    print(output)