## giải bài
# import xml.etree.ElementTree as ET

# def word_cnt(s):
#     '''return strintg'''
#     s = s.split(' ')
    
#     dicts = {}
#     for ele in s:
#         if ele in dicts:
#             dicts[ele] += 1
#         else:
#             dicts[ele] = 1
            
#     print(dicts)
    
#     root = ET.Element('words')
#     for word, count in dicts.items():
#         word_ele = ET.SubElement(root, "words")
#         word_ele.text = word
#         count_ele = ET.SubElement(root, "count")
#         count_ele.text = str(count)
    
#     tree = ET.ElementTree(root)
#     output_file = "order.xml"
#     tree.write(output_file, xml_declaration=True, encoding = 'utf-8', method='xml')

# s = "hello world hello"
# word_cnt(s)
