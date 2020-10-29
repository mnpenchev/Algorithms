""" You receive the name of a city as a string, and you need to return a string that shows how many times each letter shows up in the string by using an asterisk (*).

For example:

"Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
As you can see, the letter c is shown only once, but with 2 asterisks.

The return string should include only the letters (not the dashes, spaces, apostrophes, etc). There should be no spaces in the output, and the different letters are separated by a comma (,) as seen in the example above.

Note that the return string must list the letters in order of their first appearence in the original string.

More examples:

"Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
"Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*" """


def get_strings(city):
    city = "".join(city.lower().split())  # get rid of all spaces and turn all characters into lower case characters
    city_list = list(city)  # next turn the city string into a list
    already = []  # this is used to hold the character which has already counted before
    city_string = ''  # this is the city string which will be returned
    for word in city_list:
        if word not in already:
            count = city_list.count(word)
            city_string += word + ":"
            for i in range(0, count):
                city_string += "*"
            city_string += ","
            already.append(word)
    return city_string[:-1]


print(get_strings("Chicago"))
print(get_strings("Bangkok"))
print(get_strings("Las Vegas"))
