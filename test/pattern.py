import re

ul_class = "_3ba8S41U2S C6YnC57T6Q"
li_class = "_3zhPg5BV4U _2hiE--seNK _3FxXcV5yvs"
div_class = "_16P0LCXnI1"
storng_class = "_1Zvv5Kme1t"


ul_pattern = re.compile(r"^_.+ .+")
result = ul_pattern.match(ul_class)
print(result.group())


li_pattern = re.compile(r"^_.+ _.+ _.+")
result = li_pattern.match(li_class)
print(result.group())

div_pattern = re.compile(r"^_.+")
result = div_pattern.match(div_class)
print(result.group())
