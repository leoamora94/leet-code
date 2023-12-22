<h2>8. String to Integer (atoi)</h2>
<h3>Medium</h3>
<hr>
<div>
<p>Implement the <code>myAtoi(string s)</code> function, which converts a string to a 32-bit signed integer (similar to C/C++'s <code>atoi</code> function).</p>

<p>The algorithm for <code>myAtoi(string s)</code> is as follows:</p>

<p>1. Read in and ignore any leading whitespace.</p>
<p>2. Check if the next character (if not already at the end of the string) is <code>'-'</code> or <code>'+'</code>. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.</p>
<p>3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.</p>
<p>4. Convert these digits into an integer (i.e. <code>"123" -> 123</code>, <code>"0032" -> 32</code>). If no digits were read, then the integer is <code>0</code>. Change the sign as necessary (from step 2).</p>
<p>5. If the integer is out of the 32-bit signed integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then clamp the integer so that it remains in the range. Specifically, integers less than <code>-2<sup>31</sup></code> should be clamped to <code>-2<sup>31</sup></code>, and integers greater than <code>2<sup>31</sup> - 1</code> should be clamped to <code>2<sup>31</sup> - 1</code>.</p>
<p>6. Return the integer as the final result.</p>

<p><b>Note:</b></p>
<ul>
<li>Only the space character <code>' '</code> is considered a whitespace character.
<li><b>Do not ignore</b> any characters other than the leading whitespace or the rest of the string after the digits.
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "42"
<strong>Output:</strong> 42
<strong>Explanation:</strong> The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "    -42"
<strong>Output:</strong> -42
<strong>Explanation:</strong>
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "4193 with words"
<strong>Output:</strong> 4193
<strong>Explanation:</strong>
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.</pre>



<p>&nbsp;</p>

<p><b>Constraints:</b></p>
<ul>
<li><code>0 &lt;= s.length &lt;= 200</code>
<li><code>s</code> consists of English letters (lower-case and upper-case), digits <code>(0-9)</code>, <code>' '</code>, <code>'+'</code>, <code>'-'</code>, and <code>'.'</code>.
</ul>
</div>