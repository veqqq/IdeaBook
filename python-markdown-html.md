<!DOCTYPE html>
#### https://www.devdungeon.com/content/convert-markdown-html-python
<html>
<head>
      
  <div id="table-of-contents-links">
    <a name="table-of-contents"></a>
    <ul class="toc-node-bullets"><li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-1"><span class="toc-text">Introduction</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-2"><span class="toc-text">Setup</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-3"><span class="toc-text">Convert Markdown to HTML in Python</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-4"><span class="toc-text">Convert Markdown to HTML with command-line tool</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-5"><span class="toc-text">Generate a table of contents (TOC)</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-6"><span class="toc-text">Fenced code blocks</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-7"><span class="toc-text">Source code syntax highlighting</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-8"><span class="toc-text">Conclusion</span></a></li>
<li class="toc-node-level-1"><a href="/content/convert-markdown-html-python#toc-9"><span class="toc-text">References</span></a></li>
</ul>


<p><a href="https://github.com/Python-Markdown/markdown">Python-Markdown</a> is a package
that converts content in <a href="https://daringfireball.net/projects/markdown/">Markdown format</a> to HTML. In this example, we will look at how to convert Markdown to HTML and automatically generate a table-of-contents.
We will also look at using the command-line tool to convert content.
We will also cover how to use fenced code blocks and</p>

<div class="toc-item-anchor"><a name="toc-2"></a></div><h2 class=" toc-headings">Setup</h2>

<p>Install the <code>markdown</code> library with <code>pip</code>. I am using Python 3.8 in this example.</p>

<pre><code class="bash">python -m pip install markdown
</code></pre>

<div class="toc-item-anchor"><a name="toc-3"></a></div><h2 class=" toc-headings">Convert Markdown to HTML in Python</h2>

<p>The easiest way to convert is just use a string for input and a string for output.</p>

<pre><code class="python">import markdown

# Simple conversion in memory
md_text = '# Hello\n\n**Text**'
html = markdown.markdown(md_text)
print(html)
</code></pre>

<p>To use files for input and output instead:</p>

<pre><code class="python">import markdown

markdown.markdownFromFile(
    input='input.md',
    output='output.html',
    encoding='utf8',
)
</code></pre>

<div class="toc-item-anchor"><a name="toc-4"></a></div><h2 class=" toc-headings">Convert Markdown to HTML with command-line tool</h2>

<p>The <a href="https://python-markdown.github.io/cli/">Python-Markdown CLI tool</a> is convenient when
you just want to convert a document without embedding the code in a larger application.</p>

<p>The easiest way to invoke it by running is a module with <code>python -m</code>. For example:</p>

<pre><code class="bash"># Convert from a file
python -m markdown input.md

# Convert using STDIN/STDOUT
cat input.md | python -m markdown &gt; output.html

# Load extensions with -x (e.g. Table of contents)
python -m markdown -x toc input.md
</code></pre>

<div class="toc-item-anchor"><a name="toc-5"></a></div><h2 class=" toc-headings">Generate a table of contents (TOC)</h2>

<p>To generate a TOC, we need to using the <a href="https://python-markdown.github.io/extensions/toc/">toc extension</a>. There are a number of other extensions available
with the package that you can check out at <a href="https://python-markdown.github.io/extensions/">https://python-markdown.github.io/extensions/</a>.</p>

<p>You convert the same way before, except this time you pass in an extra parameter to include the extension</p>

<pre><code class="python">import markdown

md_text = '[TOC]\n# Title\n**text**'
html = markdown.markdown(md_text, extensions=['toc'])
print(html)
</code></pre>

<p>To customize options, you need to include the <code>markdown.extensions.toc.TocExtension</code> class
and pass an instance of that object to the extensions parameter. See the following example.
Read more at <a href="https://python-markdown.github.io/extensions/toc/#usage">https://python-markdown.github.io/extensions/toc/#usage</a></p>

<p>In your Markdown, add <code>[TOC]</code> to the Markdown where the TOC should go.</p>

<pre><code class="python">import markdown
from markdown.extensions.toc import TocExtension

md_text = '[TOC]\n# Title\n**text**'
# baselevel=2 sets headings to start at `h2`
html = markdown.markdown(md_text, extensions=[TocExtension(baselevel=2, title='Contents')])
print(html)
</code></pre>

<div class="toc-item-anchor"><a name="toc-6"></a></div><h2 class=" toc-headings">Fenced code blocks</h2>

<p>To make a code block you can indent all lines by 4 spaces by default.
Personally, I prefer using the three backticks (```) to enclose code without indenting.
It also gives a place to define which language is being used.</p>

<p>To use the triple backticks you need to enable the <code>fenced_code</code> extension.
This extensions already comes with Python-Markdown.
This will wrap the code block with a <code>&lt;pre&gt;</code> and <code>&lt;code&gt;</code> tag.</p>

<pre><code class="python">import markdown

md_text = """
# Title

```python
# some code block
```
"""
html = markdown.markdown(md_text, extensions=['fenced_code'])
print(html)
</code></pre>

<p>TIP: If you need to write a triple backtick code block within your Markdown code, you can wrap the outermost
codeblock with additional backticks. For example, use a set of 4 or 5 instead of 3 like this:</p>

<pre><code class="markdown">This is a **Markdown** file.

Here is an example of some code:

````python
# This python code contains triple backticks
markdown_text = """
```python
print(5 * 5)
```
"""
print(markdown_text)
````
</code></pre>

<div class="toc-item-anchor"><a name="toc-7"></a></div><h2 class=" toc-headings">Source code syntax highlighting</h2>

<p>To build on the previous section using <code>fenced_code</code>, you can add syntax highlighting
with the <code>codehilite</code> extension. This extensions already comes with Python-Markdown, but
it depends on another Python library named <a href="https://pygments.org">Pygments</a>.</p>

<p>Install <code>pygments</code> with <code>pip</code>:</p>

<pre><code class="bash">python -m pip install pygments
</code></pre>

<p>Here is an example of generating HTML with both <code>fenced_code</code> and <code>codehilite</code> extensions together.</p>

<pre><code class="python">import markdown

md_text = """
```python hl_lines="1 3"
# some Python code
hi = 'Hello'
print(hi)
```
"""
html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])
print(html)
</code></pre>

<p>When you add the <code>codehilite</code> extension,
the code block is wrapped with the class <code>.codehilite</code> and many other styles will be applied.
You could write your own styles, but Pygments comes with several style sets you can use.
You can generate the different styles using a command-line tool called <code>pygmentize</code>.
Use this tool to list available color themes and to generate the styles.
Save the CSS output to a <code>.css</code> file and link it in your HTML like normal.</p>

<p>To apply the proper styles, you must generate the CSS and apply it.</p>

<pre><code class="bash"># List themes. E.g. `default`, `monokai` or `solarized-dark`
pygmentize -L
# Generate CSS styles that will apply to `.codehilite` class
pygmentize -S monokai -f html -a .codehilite &gt; static/css/codehilite.css
</code></pre>

<p>In the HTML:</p>

<pre><code class="html">&lt;link rel="stylesheet" href="/static/css/codehilite.css"/&gt;
</code></pre>

</body>
</html>

