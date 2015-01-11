

def build_template_page(lines_arr):
    tags=[]

    htmlopentag ="<html>"
    headopentag ="<head>"
    title ="<title>"+lines_arr[0]+"</title>"
    headclosetag ="</head>"
    body ="<body>"+lines_arr[1]+"</body>"
    htmlendtag ="</html>"

    tags.append(htmlopentag)
    tags.append(headopentag)
    tags.append(title)
    tags.append(headclosetag)
    tags.append(body)
    tags.append(htmlendtag)

    output_html=open("index.html",'w')

    for line in tags:
        output_html.write(line)


def input_reader(filename):

    curr_file=open(filename,'r')
    lines=curr_file.readlines()

    parsed_blocks=parse_input_line(lines)

    for obj in parsed_blocks:
        for key in obj.keys():
            print(key+":"+obj[key])


    #build_template_page(lines)


def parse_input_line(lines):
        all_blocks_arr=[]
        new_block={}
        for line in lines:
            if line.rstrip() == "x--x":
                all_blocks_arr.append(new_block)
                new_block={}
            else:
                str_arr=line.split(":")
                new_block[str_arr[0]]=str_arr[1]

        return all_blocks_arr



input_reader("Readme.md")