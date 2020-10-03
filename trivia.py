import csv
import time

with open('trivia.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    mark = 0
    percentage = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'The quiz will be set up as ' + ''.join(row))
            line_count +=1
            
        else:
            print(f'\t The category is {row[0]}, and the subject is {row[1]}. The question is "{row[2]}" \n Is the answer  \n a) {row[3]}, \n b) {row[4]} \n c) {row[5]} \n or \n d) {row[6]}.\n')
            line_count += 1
            answer = input("Please enter a letter \n")
            if(answer.upper() == str(f'{row[7]}').upper()):
                print("Correct answer\n")
                mark +=1
                time.sleep(1)
            else:
                print("Wrong answer")
                print(f" The correct answer is {row[7]} \n")

            
    print(f'You have gotten ' + str(mark) + f' marks out of {line_count - 1} questions.')
    percentage =  int((mark / (line_count - 1)) * 100)

    if percentage == 100:
        print("Oh yeah. This is the good stuff. Great job on the " + str(percentage) + " per cent, my boy. Just be wary regardless")
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

