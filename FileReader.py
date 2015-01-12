import os
import sys

def blank_template(file_as_array):
    file_as_array.append("<html>")


def create_tag(tag_obj):

    content_present=False

    # store the tag name
    tag_name=tag_obj['type']

    # remove the type details
    del tag_obj['type']

    #start building the tag
    tag="<"+tag_name+" "
    style_tag=" style='"

    for tag_key in tag_obj.keys():
        if tag_key=='content':
            content_present=True
        elif tag_key=='src':
            tag=tag+tag_key+"='"+tag_obj[tag_key]+"' "
        elif tag_key=='href':
            tag=tag+tag_key+"='"+tag_obj[tag_key]+"' "
        else:
            style_tag=style_tag+tag_key+":"+tag_obj[tag_key]+";"


    style_tag=style_tag+"'"

    if tag_name=='title':
        tag="<head>"+tag
    else:
        tag=tag+style_tag

    if content_present:
        tag=tag+">"
        tag=tag+tag_obj['content']
        if tag_name!='body' and tag_name!='div':
            tag=tag+"</"+tag_name+"><br>"

        if tag_name=='title':
            tag=tag+"</head>"

    elif tag_name=='div'or tag_name=='body':
        tag=tag+">"
    else:
            tag = tag+"/><br>"

    return tag

def build_template_page(parsed_blocks):

    file_as_an_array=[]
    blank_template(file_as_an_array)

    for tag_obj in parsed_blocks:
        #tag_obj is a dictionary
        # close the head before opening body

        tag=create_tag(tag_obj)
        file_as_an_array.append(tag)
        file_as_an_array.append('\n')

    file_as_an_array.append("</div>")
    file_as_an_array.append("</body>")
    file_as_an_array.append("</html>")


    return file_as_an_array

def print_all_dictionaries(parsed_blocks):

    for obj in parsed_blocks:
        for key in obj.keys():
            print(key+":"+obj[key])


def create_HTML_page(file_as_arr,count):

   # if os.path.isfile('index.html'):
   #     os.remove('index.html')

    filename = 'index'+str(count)+'.html'

    output_file = open('./output_folder/'+filename,'w')
    output_file.writelines(file_as_arr)

def input_reader(filename,count):

    curr_file=open(filename,'r')
    lines = curr_file.readlines()

    # generates all the dictionaries for output
    parsed_blocks = parse_input_line(lines)

    # prints all dictionaries
    print_all_dictionaries(parsed_blocks)

    #building the html template
    file_as_arr = build_template_page(parsed_blocks)

    #create the actual HTML page
    create_HTML_page(file_as_arr,count)

    os.remove('./input_folder/input.txt')

def parse_input_line(lines):
        all_blocks_arr = []
        new_block = {}
        for line in lines:
            if line.rstrip() == "x--x":
                all_blocks_arr.append(new_block)
                new_block = {}
            else:
                str_arr = line.split(":")
                new_block[str_arr[0]]=str_arr[1].rstrip()

        return all_blocks_arr

#input_reader(sys.argv[1])