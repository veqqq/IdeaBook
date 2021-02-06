<!DOCTYPE html>
##### https://www.devdungeon.com/content/web-scraping-go

-the code snipets are badly formatted and look ugly

<html>
<head>
<ul>
    <li><a href="#intro">Introduction</a></li>
    <li><a href="#ethics_and_guidelines">Ethics and guidelines of scraping</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#make_http_get_request">Make an HTTP GET request</a></li>
    <li><a href="#make_http_get_request_with_timeout">Make an HTTP GET request with timeout</a></li>
    <li><a href="#set_http_headers_change_user_agent">Set HTTP headers (Change user agent)</a></li>
    <li><a href="#download_a_url">Download a URL</a></li>
    <li><a href="#substring_matching">Use substring matching to find page title</a></li>
    <li><a href="#using_regular_expressions_to_find_html_comments">Use regular expressions to find HTML comments</a></li>
    <li><a href="#find_all_links_on_page">Use goquery to find all links on a page</a></li>
    <li><a href="#parse_urls">Parse URLs</a></li>
    <li><a href="#find_all_images_on_page">Use goquery to find all images on a page</a></li>
    <li><a href="#make_http_post_request_with_data">Make an HTTP POST request with data</a></li>
    <li><a href="#make_http_request_with_cookie">Make HTTP request with cookie</a></li>
    <li><a href="#log_in_to_website">Log in to a website</a></li>
    <li><a href="#crawling">Web crawling</a></li>
    <li><a href="#webgenome_project">DevDungeon Project: Web Genome - http://www.webgeno.me</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
</ul>



<a name="intro"></a>
<h2>Introduction</h2>

<p>Web scraping (<a href="https://en.wikipedia.org/wiki/Web_scraping" target="_blank">Wikipedia entry</a>) is a handy tool to have in your arsenal. It can be useful in a variety of situations, like when a website does not provide an API, or you need to parse and extract web content programmatically. This tutorial walks through using the standard library to perform a variety of tasks like making requests, changing headers, setting cookies, using regular expressions, and parsing URLs. It also covers the basics of the <strong>goquery</strong> package (a jQuery like tool) to scrape information from an HTML web page on the internet.</p>

<p>If you need to reverse engineering a web application based on the network traffic, it may also be helpful to learn how to do <a href="/content/packet-capture-injection-and-analysis-gopacket">packet capture, injection, and analysis with Gopacket</a>.</p>

<p>If you are downloading and storing content from a site you scrape, you may be interested in <a href="/content/working-files-go">working with files in Go</a>.


<a name="ethics_and_guidelines"></a>
<h2>Ethics and guidelines of scraping</h2>

<p>Before doing any web scraping, it is important to understand what you are doing technically. If you use this information irresponsibly, you could potentially cause a denial-of-service, incur bandwidth costs to yourself or the website provider, overload log files, or otherwise stress computing resources. If you are unsure of the repercussions of your actions, do not perform any scraping without consulting a knowledgable person. You are responsible for the actions you take including any cost or repercussion that comes along with it.</p>

<p>When doing any scraping or crawling, you should be considerate of the server owners and use good rate limiting, prevent overloading a single site, and use reasonable settings and limits.</p>

<p>It is important to understand that some sites have terms of service that do not allow scraping. While you might not face legal problems, they could ban your account if you have one, block your IP address, or otherwise revoke your access to the website or service. Before scraping any site, find out if there are any rules or guidelines explicitly stated in the terms of service.</p>

<o>Also keep in mind that some websites do provide APIs. Check to see if an API is avaiable before scraping. If a website or service provides an API, you should use that. APIs are intended to be used programmatically and are also much more efficient.</o>



<a name="prerequisites"></a>
<h2>Prerequisites</h2>

<ul>
 <li><a href="https://golang.org" target="_blank">Go</a> - The Go programming language (tested with 1.6)</p></li>
 <li><a href="https://github.com/PuerkitoBio/goquery" target="_blank">goquery</a> (for some examples) - Go version of jQuery for DOM parsing</li>
</ul>

<p>The only dependency, other than Go itself, is the goquery package. Goquery is not needed for every example, as the majority of examples rely only on the standard library. To install the <strong>goquery</strong> dependency, use <strong>go get</strong>:</p>

<pre class="prettyprint"><code>go get github.com/PuerkitoBio/goquery</code></pre>

<p>If you have issues with your $GOPATH when using <strong>go get</strong>, be sure to read up about <a href="https://golang.org/doc/code.html#Workspaces" target="_blank">Workspaces</a> and <a href="https://golang.org/doc/code.html#GOPATH" target="_blank">the GOPATH environment variable</a> and make sure you have a <strong>GOPATH</strong> set.</p>





<a name="make_http_get_request"></a>
<h2>Make an HTTP GET request</h2>
<p>The first step to web scraping is being able to make an HTTP request. Let's look a very basic HTTP GET request and how to check the response code and view the content. Note the default timeout of an HTTP request using the default <strong>transport</strong> is forever.</p>

<pre class="prettyprint"><code>// make_http_request.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;io&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br />&nbsp;&nbsp;&nbsp; &quot;os&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Make HTTP GET request<br />&nbsp;&nbsp;&nbsp; response, err := http.Get(&quot;https://www.devdungeon.com/&quot;)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; // Copy data from the response to standard output<br />&nbsp;&nbsp;&nbsp; n, err := io.Copy(os.Stdout, response.Body)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; log.Println(&quot;Number of bytes copied to STDOUT:&quot;, n)<br />}</code></pre>



<a name="make_http_get_request_with_timeout"></a>
<h2>Make an HTTP GET request with timeout</h2>
<p>When using <strong>http.Get()</strong> to make a request, it uses the default HTTP client with default settings. If you want to override the settings you need to create your own client and use that to make the request. This example demonstrates how to create an <strong>http.Client</strong> and use it to make a request.</p>

<pre class="prettyprint"><code>// make_http_request_with_timeout.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;io&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br />&nbsp;&nbsp;&nbsp; &quot;os&quot;<br />&nbsp;&nbsp;&nbsp; &quot;time&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Create HTTP client with timeout<br />&nbsp;&nbsp;&nbsp; client := &amp;http.Client{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Timeout: 30 * time.Second,<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Make request<br />&nbsp;&nbsp;&nbsp; response, err := client.Get(&quot;https://www.devdungeon.com/&quot;)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; // Copy data from the response to standard output<br />&nbsp;&nbsp;&nbsp; n, err := io.Copy(os.Stdout, response.Body)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; log.Println(&quot;Number of bytes copied to STDOUT:&quot;, n)<br />}</code></pre>



<a name="set_http_headers_change_user_agent"></a>
<h2>Set HTTP headers (Change user agent)</h2>

<p>In the first example we saw how to use the default HTTP client to make a request. Then we saw how to create out own client so we could customize the settings, like the timeout. Similarly, the HTTP clients use a default <strong>Request</strong> type which we can also customize. This example will walk through creating a request and modifying the headers before sending.</p>

<p>I highly recommed being a good net citizen and providing a descriptive user agent with a string that is easily parsable with a regular expression and contains a link to a website or GitHub repo so a network admin can learn about what the bot is and rate limit or block your bot if it causes problems.</p>

<pre class="prettyprint"><code># Example of a decent bot user agent<br />MyScraperBot v1.0 https://www.github.com/username/MyNanoBot - This bot does x, y, z</code></pre>

<p>Another reason to change your user agent might be to impersonate a different user agent. The default Go user agent may get blocked and you might have to impersonate a Firefox browser. It can also be useful for testing applications to see how they behave when various mobile and desktop user agents are presented.</p>

<p>This example will demonstrate how to change the HTTP headers before sending your request. To set your user agent, you will need to add/override the User-Agent header. Note you can change any header this way, including your cookies, if you wanted to manually manage them. We'll talk more about the cookies later. This only requires the standard library.</p>

<pre class="prettyprint"><code>// http_request_change_headers.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;io&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br />&nbsp;&nbsp;&nbsp; &quot;os&quot;<br />&nbsp;&nbsp;&nbsp; &quot;time&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Create HTTP client with timeout<br />&nbsp;&nbsp;&nbsp; client := &amp;http.Client{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Timeout: 30 * time.Second,<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Create and modify HTTP request before sending<br />&nbsp;&nbsp;&nbsp; request, err := http.NewRequest(&quot;GET&quot;, &quot;https://www.devdungeon.com&quot;, nil)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; request.Header.Set(&quot;User-Agent&quot;, &quot;Not Firefox&quot;)<br /><br />&nbsp;&nbsp;&nbsp; // Make request<br />&nbsp;&nbsp;&nbsp; response, err := client.Do(request)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; // Copy data from the response to standard output<br />&nbsp;&nbsp;&nbsp; _, err = io.Copy(os.Stdout, response.Body)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />}</code></pre>





<a name="download_a_url"></a>
<h2>Download a URL</h2>
<p>You may want to simply download the contents of a page and store it for offline review at a later date, or download a binary file after determining what URL contains the file you want. This example demonstrates how to make an HTTP request and stream the contents to a file. This only requires the standard library.</p>
<code>// download_url.go
package main

import (
    "io"
    "log"
    "net/http"
    "os"
)

func main() {
    // Make request
    response, err := http.Get("https://www.devdungeon.com/archive")
    if err != nil {
        log.Fatal(err)
    }
    defer response.Body.Close()

    // Create output file
    outFile, err := os.Create("output.html")
    if err != nil {
        log.Fatal(err)
    }
    defer outFile.Close()

    // Copy data from HTTP response to file
    _, err = io.Copy(outFile, response.Body)
    if err != nil {
        log.Fatal(err)
    }
}</code>





<a name="substring_matching"></a>
<h2>Use substring matching to find page title</h2>
<p>Probably the simplest way to search for something in an HTML document is to do a regular substring match. You will need to first convert the response in to a string and then use the <strong>strings</strong> package in the standard library to do substring searches. This is not my preferred way of searching for things, but it can be viable depending on what you are looking for. It is definitely worth knowing and understanding this technique in case you want to use it. Thanks <a href="https://www.reddit.com/r/golang/comments/86xrek/web_scraping_with_go/dw9i8yb/" target="_blank">xiegeo</a> for reminding me to include this section.</p>

<p>Next we will look at using regular expressions, which are even more powerful than simple substring matches. After that, we'll look at using the <strong>goquery</strong> package to parse the HTML DOM and look for data in a structured way using jQuery like syntax.</p>

<pre class="prettyprint"><code>// substring_matching.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;fmt&quot;<br />&nbsp;&nbsp;&nbsp; &quot;io/ioutil&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br />&nbsp;&nbsp;&nbsp; &quot;os&quot;<br />&nbsp;&nbsp;&nbsp; &quot;strings&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Make HTTP GET request<br />&nbsp;&nbsp;&nbsp; response, err := http.Get(&quot;https://www.devdungeon.com/&quot;)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; // Get the response body as a string<br />&nbsp;&nbsp;&nbsp; dataInBytes, err := ioutil.ReadAll(response.Body)<br />&nbsp;&nbsp;&nbsp; pageContent := string(dataInBytes)<br /><br />&nbsp;&nbsp;&nbsp; // Find a substr<br />&nbsp;&nbsp;&nbsp; titleStartIndex := strings.Index(pageContent, &quot;&lt;title&gt;&quot;)<br />&nbsp;&nbsp;&nbsp; if titleStartIndex == -1 {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fmt.Println(&quot;No title element found&quot;)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; os.Exit(0)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; // The start index of the title is the index of the first<br />&nbsp;&nbsp;&nbsp; // character, the &lt; symbol. We don&#039;t want to include<br />&nbsp;&nbsp;&nbsp; // &lt;title&gt; as part of the final value, so let&#039;s offset<br />&nbsp;&nbsp;&nbsp; // the index by the number of characers in &lt;title&gt;<br />&nbsp;&nbsp;&nbsp; titleStartIndex += 7<br /><br />&nbsp;&nbsp;&nbsp; // Find the index of the closing tag<br />&nbsp;&nbsp;&nbsp; titleEndIndex := strings.Index(pageContent, &quot;&lt;/title&gt;&quot;)<br />&nbsp;&nbsp;&nbsp; if titleEndIndex == -1 {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fmt.Println(&quot;No closing tag for title found.&quot;)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; os.Exit(0)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // (Optional)<br />&nbsp;&nbsp;&nbsp; // Copy the substring in to a separate variable so the<br />&nbsp;&nbsp;&nbsp; // variables with the full document data can be garbage collected<br />&nbsp;&nbsp;&nbsp; pageTitle := []byte(pageContent[titleStartIndex:titleEndIndex])<br /><br />&nbsp;&nbsp;&nbsp; // Print out the result<br />&nbsp;&nbsp;&nbsp; fmt.Printf(&quot;Page title: %s\n&quot;, pageTitle)<br />}</code></pre>






<a name="using_regular_expressions_to_find_html_comments"></a>
<h2>Use regular expressions to find HTML comments</h2>
<p>
Regular expressions are a powerful way of searching for text patterns. I am providing one example of using regular expressions for reference, but I do not recommend using this method unless you have no other choice. In the next examples, I will look at using goquery, an easier way of finding data in a structured HTML document.
</p>
<pre class="prettyprint"><code>// find_html_comments_with_regex.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;fmt&quot;<br />&nbsp;&nbsp;&nbsp; &quot;io/ioutil&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br />&nbsp;&nbsp;&nbsp; &quot;regexp&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Make HTTP request<br />&nbsp;&nbsp;&nbsp; response, err := http.Get(&quot;https://www.devdungeon.com&quot;)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; // Read response data in to memory<br />&nbsp;&nbsp;&nbsp; body, err := ioutil.ReadAll(response.Body)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(&quot;Error reading HTTP body. &quot;, err)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Create a regular expression to find comments<br />&nbsp;&nbsp;&nbsp; re := regexp.MustCompile(&quot;&lt;!--(.|\n)*?--&gt;&quot;)<br />&nbsp;&nbsp;&nbsp; comments := re.FindAllString(string(body), -1)<br />&nbsp;&nbsp;&nbsp; if comments == nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fmt.Println(&quot;No matches.&quot;)<br />&nbsp;&nbsp;&nbsp; } else {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for _, comment := range comments {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fmt.Println(comment)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; }<br />}</code></pre>









<a name="find_all_links_on_page"></a>
<h2>Use goquery to find all links on a page</h2>
<p>This example will make use of the goquery package to parse the HTML DOM and let us search for specific elements in a convenient, jQuery-like way. We perform the HTTP request like normal, and then create a goquery document using the response. With the goquery document object, we can call <strong>Find()</strong> and process each element found. In this case, we will search for <strong>a</strong> elements, or links.</p>

<p>I am only scratching the surface of what <a href="https://github.com/PuerkitoBio/goquery" target="_blank">goquery</a> can do. Here is an example of what it can do:</p>

<pre class="prettyprint"><code>// Example of a more complex goquery to find an element in the DOM<br />// https://github.com/PuerkitoBio/goquery<br />document.Find(&quot;.sidebar-reviews article .content-block&quot;)</code></pre>

<p>This is a full working example of how to use goquery to find all the links on a page and print them out.</p>

<pre class="prettyprint"><code>// find_links_in_page.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;fmt&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br /><br />&nbsp;&nbsp;&nbsp; &quot;github.com/PuerkitoBio/goquery&quot;<br />)<br /><br />// This will get called for each HTML element found<br />func processElement(index int, element *goquery.Selection) {<br />&nbsp;&nbsp;&nbsp; // See if the href attribute exists on the element<br />&nbsp;&nbsp;&nbsp; href, exists := element.Attr(&quot;href&quot;)<br />&nbsp;&nbsp;&nbsp; if exists {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fmt.Println(href)<br />&nbsp;&nbsp;&nbsp; }<br />}<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Make HTTP request<br />&nbsp;&nbsp;&nbsp; response, err := http.Get(&quot;https://www.devdungeon.com&quot;)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; // Create a goquery document from the HTTP response<br />&nbsp;&nbsp;&nbsp; document, err := goquery.NewDocumentFromReader(response.Body)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(&quot;Error loading HTTP response body. &quot;, err)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Find all links and process them with the function<br />&nbsp;&nbsp;&nbsp; // defined earlier<br />&nbsp;&nbsp;&nbsp; document.Find(&quot;a&quot;).Each(processElement)<br />}</code></pre>





<a name="parse_urls"></a>
<h2>Parse URLs</h2>
<p>In the previous example we looked at finding all the links on a page. A common task after that is to examine the URL and determine if it is a relative URL that leads somewhere on the same site, or a URL that leads off-site somewhere. You can use the string functions to search and parsae the URL manually, but there is a better way!</p>
<p>The Go standard library provides a convenient <strong>URL</strong> type that can handle all of the URL string parsing for us. Let it handle the heavy lifting with string parsing, and just get the hostname, port, query, requestURI, using the predefined functions. Read more about the <strong>url</strong> package and the <strong>url.URL</strong> type at <a href="https://golang.org/pkg/net/url/" target="_blank">https://golang.org/pkg/net/url/</a>.</p>
<pre class="prettyprint"><code>// parse_urls.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;fmt&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/url&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Parse a complex URL<br />&nbsp;&nbsp;&nbsp; complexUrl := &quot;https://www.example.com/path/to/?query=123&amp;this=that#fragment&quot;<br />&nbsp;&nbsp;&nbsp; parsedUrl, err := url.Parse(complexUrl)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Print out URL pieces<br />&nbsp;&nbsp;&nbsp; fmt.Println(&quot;Scheme: &quot; + parsedUrl.Scheme)<br />&nbsp;&nbsp;&nbsp; fmt.Println(&quot;Host: &quot; + parsedUrl.Host)<br />&nbsp;&nbsp;&nbsp; fmt.Println(&quot;Path: &quot; + parsedUrl.Path)<br />&nbsp;&nbsp;&nbsp; fmt.Println(&quot;Query string: &quot; + parsedUrl.RawQuery)<br />&nbsp;&nbsp;&nbsp; fmt.Println(&quot;Fragment: &quot; + parsedUrl.Fragment)<br /><br />&nbsp;&nbsp;&nbsp; // Get the query key/values as a map<br />&nbsp;&nbsp;&nbsp; fmt.Println(&quot;\nQuery values:&quot;)<br />&nbsp;&nbsp;&nbsp; queryMap := parsedUrl.Query()<br />&nbsp;&nbsp;&nbsp; fmt.Println(queryMap)<br /><br />&nbsp;&nbsp;&nbsp; // Craft a new URL from scratch<br />&nbsp;&nbsp;&nbsp; var customURL url.URL<br />&nbsp;&nbsp;&nbsp; customURL.Scheme = &quot;https&quot;<br />&nbsp;&nbsp;&nbsp; customURL.Host = &quot;google.com&quot;<br />&nbsp;&nbsp;&nbsp; newQueryValues := customURL.Query()<br />&nbsp;&nbsp;&nbsp; newQueryValues.Set(&quot;key1&quot;, &quot;value1&quot;)<br />&nbsp;&nbsp;&nbsp; newQueryValues.Set(&quot;key2&quot;, &quot;value2&quot;)<br />&nbsp;&nbsp;&nbsp; customURL.Fragment = &quot;bookmarkLink&quot;<br />&nbsp;&nbsp;&nbsp; customURL.RawQuery = newQueryValues.Encode()<br /><br />&nbsp;&nbsp;&nbsp; fmt.Println(&quot;\nCustom URL:&quot;)<br />&nbsp;&nbsp;&nbsp; fmt.Println(customURL.String())<br />}</code></pre>






<a name="find_all_images_on_page"></a>
<h2>Use goquery to find all images on a page</h2>
<p>
We can also leverage the <strong>goquery</strong> package to search for other elements. This is another simple example similar to finding the links on a page. This example will show how to search for images on a page and list the URLs. This example is written slightly different, to demonstrate how to create an anonymous function to handle the processing instead of a named function.
</p>

<pre class="prettyprint"><code>// find_images_in_page.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;fmt&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br /><br />&nbsp;&nbsp;&nbsp; &quot;github.com/PuerkitoBio/goquery&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; // Make HTTP request<br />&nbsp;&nbsp;&nbsp; response, err := http.Get(&quot;https://www.devdungeon.com&quot;)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; // Create a goquery document from the HTTP response<br />&nbsp;&nbsp;&nbsp; document, err := goquery.NewDocumentFromReader(response.Body)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(&quot;Error loading HTTP response body. &quot;, err)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Find and print image URLs<br />&nbsp;&nbsp;&nbsp; document.Find(&quot;img&quot;).Each(func(index int, element *goquery.Selection) {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; imgSrc, exists := element.Attr(&quot;src&quot;)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if exists {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fmt.Println(imgSrc)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; })<br />}</code></pre>




<a name="make_http_post_request_with_data"></a>
<h2>Make HTTP POST request with data</h2>
<p>Making a POST request is similar to a GET request. In fact, it is as simple as changing the word "GET" to "POST" in the request. However, a POST request is often accompanied with a payload. This could be a binary file or a URL encoded form. This example will demonstrate how to make a POST request with URL encoded form data and how to post a file like when uploading a file..</p>
<pre class="prettyprint"><code>// http_post_with_payload.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/url&quot;<br />)<br /><br />func main() {<br /><br />&nbsp;&nbsp;&nbsp; response, err := http.PostForm(<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;http://example.com/form&quot;,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; url.Values{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;username&quot;: {&quot;MyUsername&quot;},<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;password&quot;: {&quot;123&quot;},<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; },<br />&nbsp;&nbsp;&nbsp; )<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp;&nbsp;&nbsp; defer response.Body.Close()<br /><br />&nbsp;&nbsp;&nbsp; log.Println(response.Header) // Print the response headers<br /><br />&nbsp;&nbsp;&nbsp; // To upload a file, use Post instead of PostForm, provide<br />&nbsp;&nbsp;&nbsp; // a content type like application/json or application/octet-stream,<br />&nbsp;&nbsp;&nbsp; // and then provide the an io.Reader with the data<br /><br />&nbsp;&nbsp;&nbsp; // http.Post(&quot;http://example.com/upload&quot;, &quot;image/jpeg&quot;, &amp;buff)<br />}</code></pre>





<a name="make_http_request_with_cookie"></a>
<h2>Make HTTP request with cookie</h2>
<p>Since cookies are simply HTTP headers, you can manually set and manage cookies yourself by checking and setting the header values as needed.</p>

<p>Go offers a better way of managing cookies with a <strong>Cookie</strong> type that is used by the <strong>Request</strong> and <strong>Response</strong> type. You can see the source code for the <strong>Cookie</strong> at <a href="https://golang.org/src/net/http/cookie.go" target="_blank">https://golang.org/src/net/http/cookie.go</a></p>

<p>These are some of the cookie functions available on the <strong>Request</strong> and <strong>Response</strong> types:</p>
<pre class="prettyprint"><code>// Cookie functions for Request <br />// https://golang.org/pkg/net/http/#Request<br />Request.AddCookie()&nbsp; // Add cookie to request<br />Request.Cookie()&nbsp;&nbsp;&nbsp;&nbsp; // Get specific cookie<br />Request.Cookies()&nbsp;&nbsp;&nbsp; // Get all cookies<br /><br />// Cookie functions for Response<br />// https://golang.org/pkg/net/http/#Response<br />Response.Cookies()&nbsp;&nbsp; // Get all cookies</code></pre>

<p>Alternatively, you could use a library that is not part of the standard library like the <a href="https://github.com/gorilla/sessions" target="_blank">sessions package provided by Gorilla</a>, but that will not be covered here.</p>

<p>There is also a <strong>cookiejar</strong> type. It is essentially a collection of cookies separated by URL. You can read more about at <a href="https://golang.org/pkg/net/http/cookiejar/" target="_blank">https://golang.org/pkg/net/http/cookiejar/</a>. It is useful if you need to manage cookies for multiple sites.</p>

<pre class="prettyprint"><code>// http_request_with_cookie.go<br />package main<br /><br />import (<br />&nbsp;&nbsp;&nbsp; &quot;fmt&quot;<br />&nbsp;&nbsp;&nbsp; &quot;log&quot;<br />&nbsp;&nbsp;&nbsp; &quot;net/http&quot;<br />)<br /><br />func main() {<br />&nbsp;&nbsp;&nbsp; request, err := http.NewRequest(&quot;GET&quot;, &quot;https://www.devdungeon.com&quot;, nil)<br />&nbsp;&nbsp;&nbsp; if err != nil {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log.Fatal(err)<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Create a new cookie with the only required fields<br />&nbsp;&nbsp;&nbsp; myCookie := &amp;http.Cookie{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Name:&nbsp; &quot;cookieKey1&quot;,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Value: &quot;value1&quot;,<br />&nbsp;&nbsp;&nbsp; }<br /><br />&nbsp;&nbsp;&nbsp; // Add the cookie to your request<br />&nbsp;&nbsp;&nbsp; request.AddCookie(myCookie)<br /><br />&nbsp;&nbsp;&nbsp; // Ask the request to tell us about itself,<br />&nbsp;&nbsp;&nbsp; // just to confirm the cookie attached properly<br />&nbsp;&nbsp;&nbsp; fmt.Println(request.Cookies())<br />&nbsp;&nbsp;&nbsp; fmt.Println(request.Header)<br /><br />&nbsp;&nbsp;&nbsp; // Do something with the request<br />&nbsp;&nbsp;&nbsp; // client := &amp;http.Client{}<br />&nbsp;&nbsp;&nbsp; // client.Do(request)<br />}</code></pre>


<a name="log_in_to_website"></a>
<h2>Log in to a website</h2>

<p>Logging in to a site is relatively simple conceptually. You make an HTTP POST to a specific URL containing your username and password, and it returns a cookie, which is simply an HTTP header, that contains a unique key that matches your session on the server. Most websites work the same in this regard, although custom authentication mechanisms, CAPTCHAs, two-factor authentication, and other security measures complicate this process.</p>

<p>Logging in to a site is going to have to be tailored specifically to your target website. You will have to reverse engineer the authentication process from the site. Many websites use a simple form-based login system. Inside a browser like Chrome or Firefox, you can right click on one of the form fields and choose "inspect". This will allow you to see how the form is constructed, what the target action url is, and how the form fields are named in order to recreate the request programmatically.</p>

<p>You can inspect the form in the source of the HTML, or you can monitor the network traffic itself. The brwoser extensions will let you see the POST requests going on behind the scene on a website, but you could use other tools as well like jsfiddler, burp suite, Zed Attack Proxy (ZAP), or any other man-in-the-middle proxying tool.</p>

<p>Typically, you will need to get the URL in the <strong>action</strong> attribute of the <strong>form</strong>, and the <strong>name</strong> attribute of the of the username and password <strong>input</strong> fields. Once you have that information, you can make the POST request to the URL, and then store the session cookie the server provides in its response. You will need to pass the session cookie with any subsequent requests you make to the server.</p>

<p>Because every website has it's own mechanism for authentication, I am only covering this at the conceptual level and not providing a code example.</p>



<a name="crawling"></a>
<h2>Web crawling</h2>
<p>Crawling is simply an extension of scraping. We already looked at how to <a href="#find_all_links_on_page">find all links on a page</a>, and how to <a href="#parse_urls">parse URLs</a>, which are the important steps. You want to find all the links on a page, parse the url, decide if you want to follow it, and then make a request to the new url, repeating the process.</p>

<p>After parsing a URL, you can determine whether it belongs to the same site you are already on, or leads to another website. You can also look for a file extension at the end of the URL for clues about what it leads to.</p>

<p>You can crawl in a breadth-first or a depth-first manner. One depth-first approach would be to crawl only URLs from the same website before crawling the next website in the list. A breadth-first approach would be to prioritize links that lead to websites you have never seen before.</p>

<p>For a code example of a web crawler, check out the DevDungeon Web Genome project in the next section.</p>

<a name="webgenome_project"></a>
<h2>DevDungeon Project: Web Genome</h2>
<p>Web Genome is a breadth first web crawler that stores HTTP headers in a MongoDB database with a web interface all written in Go. Read more on the <a href="/content/web-genome">Web Genome project page</a> and browse the source code at <a href="https://github.com/DevDungeon/WebGenome" target="_blank">https://github.com/DevDungeon/WebGenome</a>.</p>
<p>Visit the Web Genome website at <a href="http://www.webgeno.me" target="_blank">http://www.webgeno.me</a>.</p>



</body>
</html>

