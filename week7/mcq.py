from string import ascii_lowercase
import datetime
irish_dict = {1:"A haon", 2:"A dó", 3:"A trí"}
irish_dict = dict([(1,"A haon"), (2,"A dó"), (3,"A trí")])
# print(irish_dict.get(4, "Unknown"))
# print(irish_dict.keys())
# print(irish_dict.items())
# x = { i:i*10 for i in range(1,11) }
# print(x)
# text = "The quick brown fox jumps over a lazy dog"
# letter_frequencies = { character : ascii_lowercase.count(character) for character in text }
# print(max(letter_frequencies,key=letter_frequencies.get))
numbers = [6, 1, 5, 3, 1, 2, 6, 6, 3, 6, 7,7,7 ,7,7,7,7]
distinct_numbers = list(set(numbers))
number_frequencies = { number:numbers.count(number) for number in distinct_numbers }
# print(number_frequencies)
# print(max(number_frequencies.values()))
# end_date = datetime.date(2021,12,31)

# print(end_date.strftime("%d/%m/%Y"))
# print(datetime.datetime.fromisoformat("3/17/2022"))
# end_date = datetime.datetime.strptime("Fri Nov 05 14:32:57 GMT 2021", "%A %B %d %H:%M:%S %Z %Y")
# print(end_dat

datetime.datetime(2022, 1, 10, 5, 4, 3)