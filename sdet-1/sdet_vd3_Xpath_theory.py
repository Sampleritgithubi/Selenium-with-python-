
"""
X path
Xpath stands for xml path language, it is used to to uniquely identify or address the parts of axml

- It is a syntax or a language for finding any element  on the web page using xmlm path expression
- Xpath is used to find the location of any element on the web page using html DOM structure
- xpath can be used to navigate through elements and attributes in DOm structure
(DOM- Document object model)
- Xpath is address of an element

"DOM is an API interface provided by browser "
" When a web page is loaded the browser creates a document object model of the page"

Types of Xpath
1. Absolute/Full xpath
- Starts from nodes and tags
- It starts from root html code
- it starts with single slash /
- It absolute we use nodes and tags

2. Relative/Partial Xpath
- Directly jumps to element on DOM
- it starts with double slash //
- It Relative xpath we use atrributes(i,e- Name,id,class etc)


Syntax

1. Absolute path

It will iclude all nodes tags somewhat lengthy

/html/body/div/div[2]/div[3]/a

where,
a= element


2. Relative xpath/partial xpath

only one attribute

//Tagname[@attribute='Value']

where,
we can also replace tagname with * (Star)

Tools to get xpath

1. Firebug,firepath-(Fire fox)- deprecated for some security reason

2. In built in browser- inpect copy as xpath/ Full xpath

3. Selectors hub(Extension)- add to chrome
- Use to get xpath
- To get CSS selector
- Used to check Xpath and CSS


Interview important

Most widely used xpath? and Why?

Ans)
Relative Xpath
- Relative xpath is stable compared to absolute xpath
- Absolute xpath is length and diffcult to write

Reason why Relative is better when compared to absolute xpath

If developer includes something new in his code or If developer makes changes to a image location it
it will lead to mess up of indexing which causes absolute path to break



All Xpath options

1. and
2. contains()
3. Starts-with()
4. text()


"""