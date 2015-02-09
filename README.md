##HTML Parser

HTML Parser is a simple module to parse any website or file with any Regex you want to.

###Usage
1)<br>
import the module:<br>
<code python>
import parse.py
</code><br>

2)<br>
Build proper regex:<br>
Example: <br>
<img src="regex-shot-github.jpg"><br>

3)<br>
Use the functions of the module<br>
<code>import parse</code><br>
<code>print parse.fromFile("./doc.txt", yourRegex)</code><br>
<code>print parse.fromUrl("amazon.com/dp/foobar", yourOtherRegex)</code>
