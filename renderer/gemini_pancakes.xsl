<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" indent="yes"/>
<xsl:template match="/">
  <html>
    <head>
      <title>Gemini Pancake Renderer</title>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&amp;display=swap"/>
      <style>
        body { font-family: 'IBM Plex Mono', monospace; white-space: pre-wrap; font-size: 10pt; }
        .section { border: 1px solid #ccc; margin-bottom: 1em; padding: 1em; }
        h2 { margin-top: 1em; }
        .comment { color: green; }
        .tag { color: blue; }
      </style>
    </head>
    <body>
      <xsl:apply-templates select="answer_operator/*"/>
    </body>
  </html>
</xsl:template>

<xsl:template match="answer_operator/*">
  <div class="section">
    <h2><xsl:value-of select="name()"/> <xsl:for-each select="@*"><xsl:text> </xsl:text><xsl:value-of select="name()"/>="<xsl:value-of select="."/>"</xsl:for-each></h2>
    <xsl:apply-templates/>
  </div>
</xsl:template>

<xsl:template match="comment()">
  <span class="comment">&lt;!--<xsl:value-of select="."/>--&gt;</span>
</xsl:template>
    
<xsl:template match="*">
  <span class="tag">&lt;<xsl:value-of select="name()"/>
    <xsl:for-each select="@*"><xsl:text> </xsl:text><xsl:value-of select="name()"/>="<xsl:value-of select="."/>"</xsl:for-each>&gt;</span>
  <xsl:apply-templates/>
  <span class="tag">&lt;/<xsl:value-of select="name()"/>&gt;</span>
</xsl:template>

<xsl:template match="text()">
  <xsl:value-of select="."/>
</xsl:template>

</xsl:stylesheet>