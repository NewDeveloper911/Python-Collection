import csv
import time

def load_quiz(csv_filename):
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        line_count = 0
        mark = 0
        percentage = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'The quiz will be set up as ' + ''.join(row))
                line_count +=1
            else:
                print(f'The question is "{row[0]}" \n Is the answer  \n a) {row[1]}, \n b) {row[2]} \n c) {row[3]} \n d) {row[4]}.\n')
                line_count += 1
                answer = input("Please enter a letter \n")
                if(answer.upper() == str(f'{row[5]}').upper()):
                    print("Correct answer\n")
                    mark +=1
                    time.sleep(1)
                else:
                    print("Wrong answer")
                    print(f" The correct answer is {row[5]} \n")


        print(f'You have gotten ' + str(mark) + f' marks out of {line_count - 1} questions.')
        percentage =  int(round((mark / (line_count - 1)) * 100))
        print(percentage)

        if percentage == 100:
            print("Oh yeah. The triple digits. Splendid job on the 100%")
        elif percentage >= 85 and percentage < 100:
            print("Good job on the " + str(percentage) + "% buddy. That's an A*. This is what I'm talking about")
        elif percentage >= 80 and percentage < 85:
            print("Good job on the " + str(percentage) + "% buddy. That's an A. Now, we're getting somewhere")
        elif percentage >= 70 and percentage < 80:
            print("Good job on the " + str(percentage) + "% buddy. That's an A-. Getting better")
        elif percentage >= 60 and percentage < 70:
            print("Good job on the " + str(percentage) + "% buddy. That's an B. That's ok, I guess")
        elif percentage >= 50 and percentage < 60:
            print("Good job on the " + str(percentage) + "% buddy. That's an C. You barely passed")
        else:
            print("You failed. Study again and retake the test")

subject = input("Which subject would you like to test yourself on today?\nYour choices aere Biology, Chemistry, Physics and Business Studies.\n If it's Business Studies, please type 'bs'. \n")
if subject.upper() in ['BIOLOGY','CHEMISTRY','BS','PHYSICS']:
    csv_string = subject.lower() + '.csv'
    load_quiz(csv_string)
else:
   print("I guess you don't want to succeed in school then. Your loss")
   quit()    
    
