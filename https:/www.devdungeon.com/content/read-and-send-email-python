<!DOCTYPE html>
<html>
<body>
<head>
      
  <div id="table-of-contents-links">
    <a name="table-of-contents"></a>
    <ul class="toc-node-bullets"><li class="toc-node-level-1"><a href="/content/read-and-send-email-python#toc-1"><span class="toc-text">Introduction</span></a></li>
<li class="toc-node-level-1"><a href="/content/read-and-send-email-python#toc-2"><span class="toc-text">A note about Gmail</span></a></li>
<li class="toc-node-level-1"><a href="/content/read-and-send-email-python#toc-3"><span class="toc-text">Read email with IMAP</span></a></li>
<li class="toc-node-level-2"><a href="/content/read-and-send-email-python#toc-7"><span class="toc-text">Parse email contents</span></a></li>
<li class="toc-node-level-1"><a href="/content/read-and-send-email-python#toc-4"><span class="toc-text">Send email with SMTP</span></a></li>
<li class="toc-node-level-2"><a href="/content/read-and-send-email-python#toc-8"><span class="toc-text">Send plaintext email</span></a></li>
<li class="toc-node-level-2"><a href="/content/read-and-send-email-python#toc-9"><span class="toc-text">Send multipart HTML email with attachments</span></a></li>
<li class="toc-node-level-2"><a href="/content/read-and-send-email-python#toc-10"><span class="toc-text">Email templates with Jinja2</span></a></li>
<li class="toc-node-level-2"><a href="/content/read-and-send-email-python#toc-11"><span class="toc-text">Send a text message (SMS/MMS) via email</span></a></li>
<li class="toc-node-level-1"><a href="/content/read-and-send-email-python#toc-5"><span class="toc-text">Conclusion</span></a></li>
<li class="toc-node-level-1"><a href="/content/read-and-send-email-python#toc-6"><span class="toc-text">References</span></a></li>
</ul></div><article id="node-391" class="node node-blog node-promoted clearfix" about="/content/read-and-send-email-python" typeof="sioc:Post sioct:BlogPost"><header><span property="dc:title" content="Read and Send Email with Python" class="rdf-meta element-hidden"></span>  </header><span class="submitted">
        <span property="dc:date dc:created" content="2020-03-14T17:44:17-05:00" datatype="xsd:dateTime" rel="sioc:has_creator">Submitted by <a href="/users/nanodano" title="View user profile." class="username" xml:lang="" about="/users/nanodano" typeof="sioc:UserAccount" property="foaf:name" datatype="">NanoDano</a> on Sat, 03/14/2020 - 17:44</span>    </span>
      <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><!-- # Read and Send Email with Python -->

<div class="toc-item-anchor"><a name="toc-1"></a></div><h2 class=" toc-headings">Introduction</h2>

<p>Python 3 has built-in libraries for IMAP, POP3, and SMTP. We will focus on learning how to send mail with SMTP and read/manage email with IMAP. We will also look at how to send an SMS text message using email.</p>

<p>If you need your own email hosting, check out <a href="https://www.interserver.net/r/181309">Interserver.net hosting</a> where you can host unlimited emails for unlimited domains as cheap as $4/month. You could also set up your own SMTP server on a VPS, but that is a hassle.</p>

<div class="toc-item-anchor"><a name="toc-2"></a></div><h2 class=" toc-headings">A note about Gmail</h2>

<p>Gmail will not let you use IMAP or POP by default and you must enable the feature.</p>

<p>To do this, go to your Gmail settings, and choose "Enable IMAP" under the "Forwarding and POP/IMAP" tab. See: <a href="https://support.google.com/mail/answer/7126229?hl=en">Check Gmail through other email platforms</a> for more information.</p>

<p>Your username is full email address at Gmail. Both IMAP and SMTP require authentication. The server names and ports are:</p>

<ul><li><strong>imap.gmail.com:993</strong> (SSL/TLS enabled)</li>
<li><strong>smtp.gmail.com:465</strong> (SSL/TLS enabled) Port 587 for TLS/STARTTLS</li>
</ul><div class="toc-item-anchor"><a name="toc-3"></a></div><h2 class=" toc-headings">Read email with IMAP</h2>

<p>To fetch emails, you can use <a href="https://docs.python.org/3/library/poplib.html">poplib</a> for POP3 or <a href="https://docs.python.org/3/library/imaplib.html">imaplib</a> to use IMAP4. We will focus only on IMAP which give you more options.</p>

<p>Use <a href="https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4">IMAP4</a> or <a href="https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_SSL">IMAP4_SSL</a> class depending on whether you are using SSL.
This example will use <code>IMAP4_SSL</code>.</p>

<ul><li>Port 143 - Default unencrypted IMAP port</li>
<li>Port 993 - Default SSL IMAP port</li>
</ul><pre><code>imaplib.IMAP4(host='', port=IMAP4_PORT)

imaplib.IMAP4_SSL(host='', port=IMAP4_SSL_PORT, keyfile=None, certfile=None, ssl_context=None)
</code></pre>

<p>To keep the first example simple, this is a minimal simple example
of checking an inbox:</p>

<pre><code class="python">import imaplib
# Connect to inbox
imap_server = imaplib.IMAP4_SSL(host='mail.example.com')
imap_server.login('nanodano@devdungeon.com', '$ecret')
imap_server.select()  # Default is `INBOX`

# Find all emails in inbox and print out the raw email data
_, message_numbers_raw = imap_server.search(None, 'ALL')
for message_number in message_numbers_raw[0].split():
    _, msg = imap_server.fetch(message_number, '(RFC822)')
    print(msg[0][1])
</code></pre>

<p>This next example will show how to do more common operations like:</p>

<ul><li>Connect to IMAP server</li>
<li>List folders (mailboxes)</li>
<li>Create, rename, and delete folders (mailboxes)</li>
<li>Search emails</li>
<li>Fetch emails</li>
<li>Mark an email as read or unread</li>
<li>Move an email to a different folder</li>
<li>Delete an email</li>
</ul><pre><code class="python">import imaplib

# Connect and login to IMAP mail server
username = 'me@example.com'
password = 'password'
mail_server = 'mail.example.com'
imap_server = imaplib.IMAP4_SSL(host=mail_server)
imap_server.login(username, password)

# List mailboxes (folders)
response_code, folders = imap_server.list()
print(response_code)  # OK
print('Available folders(mailboxes) to select:')
for folder_details_raw in folders:
    folder_details = folder_details_raw.decode().split()
    print(f'- {folder_details[-1]}')

# Create, rename, and delete mailboxes (folders)
# This format is the one my email provider interserver.net uses
# Create a mailbox
response_code, response_details = imap_server.create('INBOX.myfavorites')
print(response_code)  # `OK` on success or `NO` on failure
print(response_details)  # Create completed/Mailbox already exists
# Rename a mailbox
imap_server.rename('INBOX.myfavorites', 'INBOX.faves')
# Delete a mailbox
imap_server.delete('INBOX.faves')

# Choose the mailbox (folder) to search
# Case sensitive!
imap_server.select('INBOX')  # Default is `INBOX`

# Search for emails in the mailbox that was selected.
# First, you need to search and get the message IDs.
# Then you can fetch specific messages with the IDs.
# Search filters are explained in the RFC at:
# https://tools.ietf.org/html/rfc3501#section-6.4.4
search_criteria = 'ALL'
charset = None  # All
respose_code, message_numbers_raw = imap_server.search(charset, search_criteria)
print(f'Search response: {respose_code}')  # e.g. OK
print(f'Message numbers: {message_numbers_raw}')  # e.g. ['1 2'] A list, with string of message IDs
message_numbers = message_numbers_raw[0].split()

# Fetch full message based on the message numbers obtained from search
for message_number in message_numbers:
    response_code, message_data = imap_server.fetch(message_number, '(RFC822)')
    print(f'Fetch response for message {message_number}: {response_code}')
    print(f'Raw email data:\n{message_data[0][1]}')

    # Mark an email read/unread.
    # Other flags you can set with store() from RFC3501 include: 
    # \Seen \Answered \Flagged \Deleted \Draft \Recent
    imap_server.store(message_number, '+FLAGS', '\SEEN')  # Mark as read
    imap_server.store(message_number, '-FLAGS', '\SEEN')  # Mark as unread

    # Copy an email to a different 
    imap_server.create('INBOX.mykeepers')
    imap_server.copy(message_number, 'INBOX.mykeepers')
    # Delete an email
    imap_server.store(message_number, '+FLAGS', '\Deleted')
    # Expunge after marking emails deleted
    imap_server.expunge()


imap_server.close()
imap_server.logout()
</code></pre>

<div class="toc-item-anchor"><a name="toc-7"></a></div><h3 class=" toc-headings">Parse email contents</h3>

<p>In the previous example we showed how to fetch the raw email data,
but it includes the headers, the body, and everything in a single blob.
That raw content is the equivalent of a <code>.eml</code> message.
Python has an <code>email</code> package that will parse this raw data and provide
us a useful object.</p>

<p>You can parse the email with <a href="https://docs.python.org/3/library/email.parser.html">email.parser</a>. There is also a function named <a href="https://docs.python.org/3/library/email.parser.html#email.message_from_bytes">email.message_from_bytes()</a>
that you can use to parse directly from the raw bytes like we will have.
Once you have the <a href="https://docs.python.org/2/library/email.message.html#email.message.Message">email.message.Message</a> you can check various aspects like if it is multipart, content type, and get the payload.</p>

<p>This example will build on top of the simple inbox check example above and demonstrate how to:</p>

<ul><li>Parse email message

<ul><li>Get to/from/cc/bcc email addresses</li>
<li>Get plain text version</li>
<li>Get html version</li>
<li>Get attachments</li>
</ul></li>
</ul><pre><code class="python">import imaplib
import email

# Connect to inbox
imap_server = imaplib.IMAP4_SSL(host='mail.example.com')
imap_server.login('nanodano@devdungeon.com', '$ecret')
imap_server.select()  # Default is `INBOX`

# Find all emails in inbox
_, message_numbers_raw = imap_server.search(None, 'ALL')
for message_number in message_numbers_raw[0].split():
    _, msg = imap_server.fetch(message_number, '(RFC822)')

    # Parse the raw email message in to a convenient object
    message = email.message_from_bytes(msg[0][1])
    print('== Email message =====')
    # print(message)  # print FULL message
    print('== Email details =====')
    print(f'From: {message["from"]}')
    print(f'To: {message["to"]}')
    print(f'Cc: {message["cc"]}')
    print(f'Bcc: {message["bcc"]}')
    print(f'Urgency (1 highest 5 lowest): {message["x-priority"]}')
    print(f'Object type: {type(message)}')
    print(f'Content type: {message.get_content_type()}')
    print(f'Content disposition: {message.get_content_disposition()}')
    print(f'Multipart?: {message.is_multipart()}')
    # If the message is multipart, it basically has multiple emails inside
    # so you must extract each "submail" separately.
    if message.is_multipart():
        print('Multipart types:')
        for part in message.walk():
            print(f'- {part.get_content_type()}')
        multipart_payload = message.get_payload()
        for sub_message in multipart_payload:
            # The actual text/HTML email contents, or attachment data
            print(f'Payload\n{sub_message.get_payload()}')
    else:  # Not a multipart message, payload is simple string
        print(f'Payload\n{message.get_payload()}')
    # You could also use `message.iter_attachments()` to get attachments only
</code></pre>

<p>Note that if you have an email on disk and you want to parse it directly
from a file, you can use the <code>email.parser.BytesParser</code> like this:</p>

<pre><code class="python">from email.parser import BytesParser

with open('some_email.eml', 'rb') as email_file:
    message = BytesParser().parse(email_file)
</code></pre>

<p>If you want to pull attachments only from an email ignoring the body,
you can use <a href="https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_attachments">iter_attachments()</a>.</p>

<div class="toc-item-anchor"><a name="toc-4"></a></div><h2 class=" toc-headings">Send email with SMTP</h2>

<p>Let's look at how to send an email using Python.
First, we'll look at sending a very basic plaintext email
using <a href="https://docs.python.org/3/library/smtplib.html">smtplib</a>.
Then we'll craft a multipart email message using the <a href="https://docs.python.org/3/library/email.message.html">email.message</a> with text, HTML, and attachments.</p>

<p>These examples will use an encrypted SSL SMTP server.
The default port for SMTP with SSL is 587.</p>

<ul><li>Port 25 - Default unencrypted SMTP port</li>
<li>Port 587 - Default encrypted SSL SMTP port</li>
<li>Port 465 - Non-standard port for SSL SMTP that is rarely used</li>
</ul><p>Note that your from address can be very important. Some firewalls and email servers will prevent your email from going through if you use a domain name that does not match the sending host, so you can't pretend to be <code>@google.com</code>.</p>

<div class="toc-item-anchor"><a name="toc-8"></a></div><h3 class=" toc-headings">Send plaintext email</h3>

<p>This first example will show the simplest example of sending a mail with SMTP.
The email will be crafted by hand, with the headers first, followed by a blank
line, followed by the plain-text body.</p>

<pre><code class="python">from smtplib import SMTP_SSL, SMTP_SSL_PORT

SMTP_HOST = 'mail.example.com'
SMTP_USER = 'nanodano@devdungeon.com'
SMTP_PASS = 'Secret!'

# Craft the email by hand
from_email = 'John Leon &lt;nanodano@devdungeon.com&gt;'  # or simply the email address
to_emails = ['nanodano@devdungeon.com', 'admin@devdungeon.com']
body = "Hello, world!"
headers = f"From: {from_email}\r\n"
headers += f"To: {', '.join(to_emails)}\r\n" 
headers += f"Subject: Hello\r\n"
email_message = headers + "\r\n" + body  # Blank line needed between headers and body

# Connect, authenticate, and send mail
smtp_server = SMTP_SSL(SMTP_HOST, port=SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)  # Show SMTP server interactions
smtp_server.login(SMTP_USER, SMTP_PASS)
smtp_server.sendmail(from_email, to_emails, email_message)

# Disconnect
smtp_server.quit()
</code></pre>

<p>Instead of creating the email as a big raw string, you can use the <a href="https://docs.python.org/3/library/email.message.html#email.message.EmailMessage">email.message.EmailMessage</a> class to manage en email easier.
This example will show how to</p>

<ul><li>Create an email message object</li>
<li>Set to and from addresses</li>
<li>Set the subject</li>
<li>Add the urgent flag</li>
<li>Set body of email</li>
</ul><pre><code class="python">from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.message import EmailMessage

# Craft the email using email.message.EmailMessage
from_email = 'John Leon &lt;nanodano@devdungeon.com&gt;'  # or simply the email address
to_emails = ['nanodano@devdungeon.com', 'admin@devdungeon.com']
email_message = EmailMessage()
email_message.add_header('To', ', '.join(to_emails))
email_message.add_header('From', from_email)
email_message.add_header('Subject', 'Hello!')
email_message.add_header('X-Priority', '1')  # Urgency, 1 highest, 5 lowest
email_message.set_content('Hello, world!')

# Connect, authenticate, and send mail
smtp_server = SMTP_SSL('mail.example.com', port=SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)  # Show SMTP server interactions
smtp_server.login('user@example.com', 'pass')
smtp_server.sendmail(from_email, to_emails, email_message.as_bytes())

# Disconnect
smtp_server.quit()
</code></pre>

<div class="toc-item-anchor"><a name="toc-9"></a></div><h3 class=" toc-headings">Send multipart HTML email with attachments</h3>

<p>To create a multipart email that contains text and HTML versions along with attachments,
you can use the <a href="https://docs.python.org/3.9/library/email.mime.html#email.mime.multipart.MIMEMultipart">email.mime.multipart.MIMEMultipart</a> class.</p>

<pre><code class="python">email.mime.multipart.MIMEMultipart(_subtype='mixed', boundary=None, _subparts=None, *, policy=compat32, **_params)
</code></pre>

<p>To use a <code>MIMEMultipart</code>, first create the object just like a normal <code>email.message.EmailMessage</code>. Instead of setting the content though, we will <code>attach()</code>
all of the parts, including the text version, html version, and any attachments.</p>

<p>This example will show how to create a multipart MIME email that has</p>

<ul><li>Plain-text version of email</li>
<li>HTML version of email</li>
<li>Attachments</li>
</ul><pre><code class="python">from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64

from_email = 'John Leon &lt;nanodano@devdungeon.com&gt;'  # or simply the email address
to_emails = ['nanodano@devdungeon.com', 'johndleon@gmail.com']

# Create multipart MIME email
email_message = MIMEMultipart()
email_message.add_header('To', ', '.join(to_emails))
email_message.add_header('From', from_email)
email_message.add_header('Subject', 'Hello!')
email_message.add_header('X-Priority', '1')  # Urgent/High priority

# Create text and HTML bodies for email
text_part = MIMEText('Hello world plain text!', 'plain')
html_part = MIMEText('&lt;html&gt;&lt;body&gt;&lt;h1&gt;HTML!&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;', 'html')

# Create file attachment
attachment = MIMEBase("application", "octet-stream")
attachment.set_payload(b'\xDE\xAD\xBE\xEF')  # Raw attachment data
encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment; filename=myfile.dat")

# Attach all the parts to the Multipart MIME email
email_message.attach(text_part)
email_message.attach(html_part)
email_message.attach(attachment)

# Connect, authenticate, and send mail
smtp_server = SMTP_SSL('mail.example.com', port=SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)  # Show SMTP server interactions
smtp_server.login('user@email.com', 'password')
smtp_server.sendmail(from_email, to_emails, email_message.as_bytes())

# Disconnect
smtp_server.quit()
</code></pre>

<div class="toc-item-anchor"><a name="toc-10"></a></div><h3 class=" toc-headings">Email templates with Jinja2</h3>

<p>If you want to create a text or HTML template for re-use, I recommend
<a href="https://jinja.palletsprojects.com/en/2.11.x/">Jinja2 templates</a>.</p>

<p>Here is a <em>very</em> basic example of how a Jinja2 template can be used.
Refer to the <a href="https://jinja.palletsprojects.com/en/2.11.x/">Jinja2 documentation</a>
for more details.</p>

<pre><code class="python"># pip install jinja2
from jinja2 import Template

template = Template('Hello, {{ name }}!')
print(template.render({'name': 'NanoDano'}))
</code></pre>

<div class="toc-item-anchor"><a name="toc-11"></a></div><h3 class=" toc-headings">Send a text message (SMS/MMS) via email</h3>

<p>Most cell phone service providers also offer an email gateway that lets you email an address and it will send an SMS/MMS to the cell phone.</p>

<p>For a detailed list of SMS email gateways listed by provider, check out <a href="https://en.wikipedia.org/wiki/SMS_gateway">SMS gateways on Wikipedia</a>.</p>

<p>For example, to text the number 888-123-4567 on AT&amp;T, I could send an email to:</p>

<pre><code>8881234567@txt.att.net
</code></pre>
      
</body>
</html>

