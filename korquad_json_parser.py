import json
import os

for file_number in range(5):

    with open(f'/Users/inyeongkim/Desktop/javic/korquad/korquad_ref/KorQuAD_2.1_dev/korquad2.1_dev_0{file_number}.json') as json_file:
        raw_data = json.load(json_file)

        for x in range(len(raw_data['data'])):

            result = f"categories:\n- {raw_data['data'][x]['title']}\nconversations:\n"

            for i in range(len(raw_data['data'][x]['qas'])):
                result += f"- - {raw_data['data'][x]['qas'][i]['question']}\n"
                tmp = raw_data['data'][x]['qas'][i]['answer']['text'].replace("\n", "\\n")
                result += f"  - {tmp}\n"

            try:
                directoryPath = os.getcwd() + f'/korquad2.1_dev_0{file_number}_processed'

                if not os.path.exists(directoryPath):
                    os.mkdir(directoryPath)

                # create log file
                with open(directoryPath + f'/korquad2.1_dev_0{file_number}_' + str(raw_data['data'][x]['title']) + '.txt', 'w') as fd:
                    fd.write(result)

            except OSError:
                print("ERROR : fail to create dir!")

    print(f"{file_number}-th Done!")