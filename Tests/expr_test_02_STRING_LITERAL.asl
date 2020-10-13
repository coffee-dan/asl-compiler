// Dalio, Brian A.
// dalioba
// 2019-11-01

{
  // String literal can be empty.
  "";

  // String literal can have escaped " inside.
  "\"";

  // String literal can have escaped \ inside.
  "\\";

  // Lettered string literal escapes include \a, \b, \e, \f, \n,
  // \r, \t, and \v.
  "\a\b\e\f\n\r\t\v";

  // Even when surrounded by other characters ...
  "az\ayb\bxc\ewd\fve\nuf\rtg\tsh\vri";

  // \\ becomes \ but the resulting \a should NOT be
  // considered an instance of an escape sequence.
  "\\a\\b\\e\\f\\n\\r\\t\\v";

  // Not lexical error ...
  "\\q\\s\\u\\w\\x\\y\\z";

  // Or a string literal can just be regular characters.
  "Hi, there.  I'm a string literal.";
}

