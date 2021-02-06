<!DOCTYPE html>
#### https://www.devdungeon.com/content/python-ssh-tutorial
<html>
<head>

  <div id="table-of-contents-links">
    <a name="table-of-contents"></a>
    <ul class="toc-node-bullets"><li class="toc-node-level-1"><a href="/content/python-ssh-tutorial#toc-1"><span class="toc-text">Introduction</span></a></li>
<li class="toc-node-level-1"><a href="/content/python-ssh-tutorial#toc-2"><span class="toc-text">Installation</span></a></li>
<li class="toc-node-level-1"><a href="/content/python-ssh-tutorial#toc-3"><span class="toc-text">Connect to SSH</span></a></li>
<li class="toc-node-level-2"><a href="/content/python-ssh-tutorial#toc-7"><span class="toc-text">Connect using password</span></a></li>
<li class="toc-node-level-2"><a href="/content/python-ssh-tutorial#toc-8"><span class="toc-text">Connect using SSH key</span></a></li>
<li class="toc-node-level-1"><a href="/content/python-ssh-tutorial#toc-4"><span class="toc-text">Run commands over SSH</span></a></li>
<li class="toc-node-level-1"><a href="/content/python-ssh-tutorial#toc-5"><span class="toc-text">Conclusion</span></a></li>
<li class="toc-node-level-1"><a href="/content/python-ssh-tutorial#toc-6"><span class="toc-text">References</span></a></li>
</ul></div><article id="node-394" class="node node-blog node-promoted clearfix" about="/content/python-ssh-tutorial" typeof="sioc:Post sioct:BlogPost"><header><span property="dc:title" content="Python SSH Tutorial" class="rdf-meta element-hidden"></span>  </header><span class="submitted">
       
<div class="toc-item-anchor"><a name="toc-1"></a></div><h2 class=" toc-headings">Introduction</h2>

<p>SSH (secure shell) is good for remotely managing machines using a secure connection.
Typically you will log in to a server using the command-line <code>ssh</code> tool, or something like
PuTTy or MobaXTerm. This guide will show you how to use Python to connect and run commands
over SSH using the Paramiko package.</p>

<ul><li><a href="https://docs.paramiko.org/en/stable/">Paramiko Documentation</a></li>
<li><a href="https://github.com/paramiko/paramiko">Paramiko Source on GitHub</a></li>
</ul><div class="toc-item-anchor"><a name="toc-2"></a></div><h2 class=" toc-headings">Installation</h2>

<p>The easiest way to install <code>paramiko</code> is using <code>pip</code>.</p>

<pre><code class="bash">python -m pip install paramiko
</code></pre>

<p>To install from source, clone from GitHub and then install using <code>setup.py</code>.</p>

<pre><code class="bash">git clone https://github.com/paramiko/paramiko
cd paramiko
python setup.py install
</code></pre>

<div class="toc-item-anchor"><a name="toc-3"></a></div><h2 class=" toc-headings">Connect to SSH</h2>

<p>Connect to an SSH server using 
<a href="https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.connect">paramiko.client.SSHClient.connect()</a>. The <code>hostname</code> is the only required parameter.</p>

<pre><code class="python">connect(hostname, port=22, username=None, password=None, pkey=None, key_filename=None, timeout=None, allow_agent=True, look_for_keys=True, compress=False, sock=None, gss_auth=False, gss_kex=False, gss_deleg_creds=True, gss_host=None, banner_timeout=None, auth_timeout=None, gss_trust_dns=True, passphrase=None, disabled_algorithms=None)
</code></pre>

<p>One thing to consider is what trusted known host keys you have.
You can use <code>paramiko.client.SSHClient.load_system_host_keys()</code>.
You can also explicitly load a specific known hosts file with <code>load_host_keys()</code>
and set the client to automatically accept and add unknown hosts with
<code>set_missing_host_key_policy()</code> to <code>paramiko.AutoAddPolicy</code>.
Use these options as needed. The AutoAddPolicy is not very secure
since it will trust any remote host.</p>

<div class="toc-item-anchor"><a name="toc-7"></a></div><h3 class=" toc-headings">Connect using password</h3>

<pre><code class="python">from paramiko import SSHClient

client = SSHClient()
#client.load_system_host_keys()
#client.load_host_keys('~/.ssh/known_hosts')
#client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('example.com', username='user', password='secret')
client.close()
</code></pre>

<div class="toc-item-anchor"><a name="toc-8"></a></div><h3 class=" toc-headings">Connect using SSH key</h3>

<p>Using an SSH key is more secure than using a password.
Call <code>connect()</code> just like using the password, but instead of providing
the user password, we will provide a <code>key_filename</code> and maybe a <code>passphrase</code> for the key.
The passphrase may not be needed if your private key file does not have a passphrase.</p>

<p>You can also omit the key file and let Paramiko try to find the right key automatically
in your <code>~/.ssh/</code> directory. You can turn that on by calling <code>client.look_for_keys(True)</code>.
The first example will show how to explicitly provide the key and passphrase and the second
one will show how to look for keys.</p>

<pre><code class="python"># Explicitly provide key and passphrase
from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
#client.load_system_host_keys()
#client.load_host_keys('~/.ssh/known_hosts')
#client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('example.com', username='user', key_filename='mykey.pem', passphrase='mysshkeypassphrase')
client.close()
</code></pre>

<p>This example show hows to look for keys in <code>~/.ssh/</code> automatically.</p>

<pre><code class="python">from paramiko import SSHClient

client = SSHClient()
#client.load_system_host_keys()
#client.load_host_keys('~/.ssh/known_hosts')
#client.set_missing_host_key_policy(AutoAddPolicy())

client.look_for_keys(True)
client.connect('example.com', username='user')
client.close()
</code></pre>

<div class="toc-item-anchor"><a name="toc-4"></a></div><h2 class=" toc-headings">Run commands over SSH</h2>

<p>Once you have a connection open, you can execute any command just like you
would if you were in a regular interactive SSH session.</p>

<p>This example shows how to:</p>

<ul><li>Run a command on the server</li>
<li>Provide standard input data to command</li>
<li>Read standard output and error from command</li>
<li>Get the return code of the command</li>
</ul><p>The command run in this example is the PHP interpreter with the
code provided via standard input. The output is then printed out
and the return code is checked.</p>

<pre><code class="python">from paramiko import SSHClient

# Connect
client = SSHClient()
client.load_system_host_keys()
client.connect('example.com', username='user', password='secret')

# Run a command (execute PHP interpreter)
stdin, stdout, stderr = client.exec_command('php')
print(type(stdin))  # &lt;class 'paramiko.channel.ChannelStdinFile'&gt;
print(type(stdout))  # &lt;class 'paramiko.channel.ChannelFile'&gt;
print(type(stderr))  # &lt;class 'paramiko.channel.ChannelStderrFile'&gt;

# Optionally, send data via STDIN, and shutdown when done
stdin.write('&lt;?php echo "Hello!"; sleep(2); ?&gt;')
stdin.channel.shutdown_write()

# Print output of command. Will wait for command to finish.
print(f'STDOUT: {stdout.read().decode("utf8")}')
print(f'STDERR: {stderr.read().decode("utf8")}')

# Get return code from command (0 is default for success)
print(f'Return code: {stdout.channel.recv_exit_status()}')

# Because they are file objects, they need to be closed
stdin.close()
stdout.close()
stderr.close()

# Close the client itself
client.close()
</code></pre>

</body>
</html>

