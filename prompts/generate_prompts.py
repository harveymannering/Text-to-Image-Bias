# Import libraries
import csv

# Load the list of 50 templates prompts
# Example prompt :
#   "An object belonging to a {gender}"
objects_templates = []
with open('prompt_templates.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        objects_templates.append(' '.join(row))

# Define gender words to be used in the prompts
genders = ['man', 'woman', 'boy', 'girl']

# Write prompts to a csv file
with open('prompts.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='|',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    i = 0
    # Column headers
    spamwriter.writerow(["Filename", "Seed", "Gender_Word", "Prompt"])
    for t in objects_templates:
        for g in genders:
            prompt = t.replace('{gender}', g)
            print(prompt)
            # Write a single row
            spamwriter.writerow([str(i) + '_' + g, i, g, prompt])
        i += 1