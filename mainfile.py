import EPL_Season2000_2001 as szn2000_2001
import EPL_Season2001_2002 as szn2001_2002
import EPL_Season2002_2003 as szn2002_2003
import EPL_Season2003_2004 as szn2003_2004
import EPL_Season2004_2005 as szn2004_2005
import EPL_Season2005_2006 as szn2005_2006
import EPL_Season2006_2007 as szn2006_2007
import EPL_Season2007_2008 as szn2007_2008
import EPL_Season2008_2009 as szn2008_2009
import EPL_Season2009_2010 as szn2009_2010
import EPL_Season2010_2011 as szn2010_2011
import EPL_Season2011_2012 as szn2011_2012
import EPL_Season2012_2013 as szn2012_2013
import EPL_Season2013_2014 as szn2013_2014
import EPL_Season2014_2015 as szn2014_2015
import EPL_Season2015_2016 as szn2015_2016
import EPL_Season2016_2017 as szn2016_2017
import EPL_Season2017_2018 as szn2017_2018
import EPL_Season2018_2019 as szn2018_2019
import EPL_Season2019_2020 as szn2019_2020
import EPL_Season2020_2021 as szn2020_2021
import EPL_Season2021_2022 as szn2021_2022
import EPL_Season2022_2023 as szn2022_2023
import mysql.connector
import matplotlib.pyplot as plt


htmlstring23='''

<TABLE border=2>
<TBODY>
<TR>
<TD align=center bgColor=#fcc2c8 height=16 
width=35><FONT size=2>М</FONT></TD>
<TD align=middle bgColor=#fcc2c8 height=16 
width=225><FONT size=2>Клуб</FONT></TD>
<TD align=center bgColor=#fcc2c8 height=16 
width=55><FONT size=2>Игр</FONT></TD>
<TD align=center bgColor=#fcc2c8 height=16 
width=80><FONT size=2>Победы</FONT></TD>
<TD align=center bgColor=#fcc2c8 height=16 
width=80><FONT size=2>Ничьи</FONT></TD>
<TD align=center bgColor=#fcc2c8 height=16 
width=80><FONT size=2>Пораж.</FONT></TD>
<TD align=center bgColor=#fcc2c8 height=16 
width=80><FONT size=2>Мячи</FONT></TD>
<TD align=center bgColor=#fcc2c8 height=16 
width=55><FONT size=2>Очки</FONT></TD></TR>
<tr>
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">1</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2" color="#FF0000">Манчестер
Юнайтед</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">24</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">6</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">79-31</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>80</b></font></TD>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=14 
width=35><font size="2">2</font></TD>
<TD bgColor=#cffccd height=14 width=225><b><font size="2" color="#000080">Арсенал</font></b></TD>
<TD align=center bgColor=#cffccd height=14 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=14 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd height=14 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=14 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd height=14 
width=80><font size="2">63-38</font></TD>
<TD align=center bgColor=#cffccd height=14 
width=55><font size="2"><b>70</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">3</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2" color="#000080">Ливерпуль</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">71-39</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>69</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">4</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Лидс</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">64-43</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>68</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">5</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Ипсвич</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">6</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">57-42</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>66</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">6</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Челси</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">17</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">11</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">68-45</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>61</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">7</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Сандерленд</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">15</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">11</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">46-41</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>57</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">8</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Астон
Вилла</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">13</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">15</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">46-43</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>54</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">9</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Чарльтон</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">50-57</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>52</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">10</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Саутгемптон</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">40-48</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>52</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">11</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Ньюкасл</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">15</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">44-50</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>51</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">12</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Тоттенхем</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">13</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">15</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">47-54</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>49</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">13</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Лестер</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">6</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">18</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">39-51</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>48</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">14</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Миддлсбро</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">15</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">44-44</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>42</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">15</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Вест
Хэм</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">16</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">45-50</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>42</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">16</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Эвертон</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">11</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">18</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">45-59</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>42</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">17</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2">Дерби</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">16</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">37-59</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>42</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">18</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2" color="#000080">Манчестер
Сити</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">41-65</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>34</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">19</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2" color="#000080">Ковентри</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">36-63</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>34</b></font></TD>
  </font>
</tr>
<tr>
<TD align=center bgColor=#cffccd height=16 
width=35><font size="2">20</font></TD>
<TD bgColor=#cffccd height=16 width=225><b><font size="2" color="#000080">Брэдфорд</font></b></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">5</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">11</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">22</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=80><font size="2">30-70</font></TD>
<TD align=center bgColor=#cffccd height=16 
width=55><font size="2"><b>26</b></font></TD>
</tr>
</TBODY></TABLE>'''

htmlstring22='''

<TABLE border=2>
<TBODY>
<TR>
<TD align=center bgColor=#fcc2c8 
width=35><FONT size=2>М</FONT></TD>
<TD align=middle bgColor=#fcc2c8 
width=225><FONT size=2>Клуб</FONT></TD>
<TD align=center bgColor=#fcc2c8 
width=55><FONT size=2>Игр</FONT></TD>
<TD align=center bgColor=#fcc2c8 
width=80><FONT size=2>Победы</FONT></TD>
<TD align=center bgColor=#fcc2c8 
width=80><FONT size=2>Ничьи</FONT></TD>
<TD align=center bgColor=#fcc2c8 
width=80><FONT size=2>Пораж.</FONT></TD>
<TD align=center bgColor=#fcc2c8 
width=80><FONT size=2>Мячи</FONT></TD>
<TD align=center bgColor=#fcc2c8 
width=55><FONT size=2>Очки</FONT></TD></TR>
<tr>
<font face="Arial">
<TD align=center bgColor=#E2E7E4 
width=35><font size="2">1</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2" color="#FF0000">&nbsp;АРСЕНАЛ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">26</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">3</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">79-36</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>87</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#E2E7E4 
width=35><font size="2">2</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2" color="#000080">&nbsp;ЛИВЕРПУЛЬ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">24</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">6</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">67-30</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>80</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#E2E7E4 
width=35><font size="2">3</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2" color="#000080">&nbsp;МАНЧЕСТЕР
  ЮНАЙТЕД</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">24</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">5</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">87-45</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>77</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#E2E7E4 
width=35><font size="2">4</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2" color="#000080">&nbsp;НЬЮКАСЛ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">21</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">74-52</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>71</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">5</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;ЛИДС</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">18</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">53-37</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>66</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">6</font></TD>
<TD bgColor=#cffccd width=225><font size="2"><b>&nbsp;ЧЕЛСИ</b></font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">66-38</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>64</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">7</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;ВЕСТ ХЭМ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">15</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">15</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">48-57</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>53</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">8</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;АСТОН
  ВИЛЛА</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">46-47</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>50</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">9</font></TD>
<TD bgColor=#cffccd width=225><font size="2"><b>&nbsp;ТОТТЕНХЕМ</b></font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">49-53</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>50</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">10</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;БЛЭКБЕРН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">55-51</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>46</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">11</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;САУТГЕМПТОН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">46-54</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>45</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">12</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;МИДДЛСБРО</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">35-47</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>45</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">13</font></TD>
<TD bgColor=#cffccd width=225><font size="2"><b>&nbsp;ФУЛХЭМ</b></font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">36-44</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>44</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">14</font></TD>
<TD bgColor=#cffccd width=225><font size="2"><b>&nbsp;ЧАРЛЬТОН</b></font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">38-49</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>44</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">15</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;ЭВЕРТОН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">11</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">45-57</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>43</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">16</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2">&nbsp;БОЛТОН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">44-62</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>40</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#cffccd 
width=35><font size="2">17</font></TD>
<TD bgColor=#cffccd width=225><font size="2"><b>&nbsp;САНДЕРЛЕНД</b></font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">18</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">29-51</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>40</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#E2E7E4 
width=35><font size="2">18</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2" color="#000080">&nbsp;ИПСВИЧ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">41-64</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>36</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#E2E7E4 
width=35><font size="2">19</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2" color="#000080">&nbsp;ДЕРБИ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">6</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">24</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">33-63</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>30</b></font></TD>
  </font>
</tr>
<tr>
<font face="Arial">
<TD align=center bgColor=#E2E7E4 
width=35><font size="2">20</font></TD>
<TD bgColor=#cffccd width=225><b><font size="2" color="#000080">&nbsp;ЛЕСТЕР</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">5</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">20</font></TD>
<TD align=center bgColor=#cffccd 
width=80><font size="2">30-64</font></TD>
<TD align=center bgColor=#cffccd 
width=55><font size="2"><b>28</b></font></TD>
  </font>
</tr>
</TBODY></TABLE>

'''
htmlstring21='''


<TABLE border=2 width="100%">
<TBODY>
<TR>
<TD align=center bgColor=#fcc2c8 
width=35 height="16">
  <p><font size="2">М</font></p>
</TD>
<TD align=middle bgColor=#fcc2c8 
width=225 height="16">
  <p style="margin-left: 3" align="left"><font size="2">Клуб</font></p>
</TD>
<TD align=center bgColor=#fcc2c8 
width=55 height="16">
  <p><font size="2">Игр</font></p>
  </TD>
<TD align=center bgColor=#fcc2c8 
width=80 height="16">
  <p><font size="2">Победы</font></p>
  </TD>
<TD align=center bgColor=#fcc2c8 
width=80 height="16">
  <p><font size="2">Ничьи</font></p>
  </TD>
<TD align=center bgColor=#fcc2c8 
width=80 height="16">
  <p><font size="2">Пораж.</font></p>
  </TD>
<TD align=center bgColor=#fcc2c8 
width=80 height="16">
  <p><font size="2">Мячи</font></p>
  </TD>
<TD align=center bgColor=#fcc2c8 
width=55 height="16">
  <p><font size="2">Очки</font></p>
  </TD></TR>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 
width=35 height="16">
  <p><font size="2">1</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font color="#FF0000" size="2">МАНЧЕСТЕР ЮНАЙТЕД</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">25</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">5</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">74-34</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>83</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 
width=35 height="16">
  <p><font size="2">2</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font color="#000080" size="2">АРСЕНАЛ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">23</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">6</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">85-42</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>78</b></font></TD>
  </font>

</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 
width=35 height="16">
  <p><font size="2">3</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2" color="#000080">НЬЮКАСЛ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">21</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">6</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">11</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">63-48</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>69</b></font></TD>
  </font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 
width=35 height="16">
  <p><font size="2">4</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">ЧЕЛСИ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">19</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">68-39</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>67</b></font></TD>
  </font>

</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">5</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">ЛИВЕРПУЛЬ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">18</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">61-41</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>64</b></font></TD>
  </font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">6</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">БЛЭКБЕРН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">52-43</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>60</b></font></TD>
  </font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="8">
  <p><font size="2">7</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="8">
  <p style="margin-left: 3"><b><font size="2">ЭВЕРТОН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="8">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="8">
  <font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="8">
  <font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="8">
  <font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="8">
  <p><font size="2">48-49</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="8">
  <font size="2"><b>59</b></font></TD>
  </font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">8</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">САУТГЕМПТОН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">43-46</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>52</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">9</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">МАНЧЕСТЕР
  СИТИ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">15</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">6</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">47-54</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>51</b></font></TD>
  </font>

</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">10</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">ТОТТЕНХЕМ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">51-62</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>50</b></font></TD>
  </font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">11</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">МИДДЛСБРО</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">15</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">48-44</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>49</b></font></TD>
  </font>

</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">12</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">ЧАРЛЬТОН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">7</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">45-56</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>49</b></font></TD>
  </font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">13</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">БИРМИНГЕМ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">41-49</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>48</b></font></TD>
  </font>

</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">14</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">ФУЛХЭМ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">13</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">41-50</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>48</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">15</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">ЛИДС</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">5</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">19</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">58-57</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>47</b></font></TD>
  </font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#cffccd 
width=35 height="16">
  <p><font size="2">16</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">АСТОН ВИЛЛА</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">9</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">17</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">42-47</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>45</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD 
width=35 height="16">
  <p><font size="2">17</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2">БОЛТОН</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">14</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">41-51</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>44</b></font></TD>
  </font>

</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 
width=35 height="16">
  <p><font size="2">18</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font size="2" color="#800080">ВЕСТ ХЭМ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">10</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">12</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">16</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">42-59</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>42</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 
width=35 height="16">
  <p><font size="2">19</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font color="#800080" size="2">ВЕСТ
  БРОМВИЧ</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">6</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">8</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">24</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">29-65</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2"><b>26</b></font></TD>
</font>
</tr>
<tr>

<TD align=center bgColor=#E2E7E4 
width=35 height="16">
  <p><font size="2">20</font></p>
</TD>
<TD bgColor=#cffccd width=225 height="16">
  <p style="margin-left: 3"><b><font color="#800080" size="2">САНДЕРЛЕНД</font></b></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <font size="2">38</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">4</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">7</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <font size="2">27</font></TD>
<TD align=center bgColor=#cffccd 
width=80 height="16">
  <p><font size="2">21-65</font></TD>
<TD align=center bgColor=#cffccd 
width=55 height="16">
  <p><b><font size="2">19</font></b></TD>
</tr>
</TBODY></TABLE>

'''

htmlstring20='''
<TBODY>
<TR><TD align=center bgColor=#fcc2c8 width=35 height="16">
<p><font size="2">М</font></p></TD>
<TD align=middle bgColor=#fcc2c8 width=225 height="16">
<p style="margin-left: 3" align="left"><font size="2">Клуб</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=55 height="16">
<p><font size="2">Игр</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80 height="16">
<p><font size="2">Победы</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80 height="16">
<p><font size="2">Ничьи</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80 height="16">
<p><font size="2">Пораж.</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80 height="16">
<p><font size="2">Мячи</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=55 height="16">
<p><font size="2">Очки</font></p></TD></TR>
<tr><font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35 height="16">
<p><font size="2">1</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2" color="#FF0000">АРСЕНАЛ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">26</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">0</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">73-26</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>90</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35 height="16">
<p><font size="2">2</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2" color="#000080">ЧЕЛСИ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">24</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">67-30</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>79</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35 height="16">
<p><font size="2">3</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2" color="#000080">МАНЧЕСТЕР ЮНАЙТЕД</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">23</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">64-35</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>75</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35 height="16">
<p><font size="2">4</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">ЛИВЕРПУЛЬ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">55-37</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>60</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#FFFFCC width=35 height="16">
<p><font size="2">5</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">НЬЮКАСЛ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">52-40</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>56</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">6</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">АСТОН ВИЛЛА</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">48-44</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>56</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">7</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">ЧАРЛЬТОН</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">51-51</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>53</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">8</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">БОЛТОН</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">48-56</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>53</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">9</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">ФУЛХЭМ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">52-46</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>52</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">10</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">БИРМИНГЕМ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">43-48</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>50</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">11</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">МИДДЛСБРО</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">44-52</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>48</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">12</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">САУТГЕМПТОН</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">44-45</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>47</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">13</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">ПОРТСМУТ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">47-54</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>45</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">14</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">ТОТТЕНХЕМ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">47-57</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>45</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">15</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">БЛЭКБЕРН</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">51-59</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>44</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="16">
<p><font size="2">16</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2">МАНЧЕСТЕР СИТИ</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">55-54</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>41</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35 height="8">
<p><font size="2">17</font></p></TD>
<TD bgColor=#cffccd width=225 height="8">
<p style="margin-left: 3"><b><font size="2">ЭВЕРТОН</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="8">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="8">
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80 height="8">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="8">
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80 height="8">
<font size="2">45-57</font></TD>
<TD align=center bgColor=#cffccd width=55 height="8">
<font size="2"><b>39</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35 height="16">
<p><font size="2">18</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2" color="#800080">ЛЕСТЕР</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">48-65</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>33</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35 height="16">
<p><font size="2">19</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2" color="#800080">ЛИДС</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">21</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">40-79</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>33</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35 height="16">
<p><font size="2">20</font></p></TD>
<TD bgColor=#cffccd width=225 height="16">
<p style="margin-left: 3"><b><font size="2" color="#800080">ВУЛВЕРХЭМПТОН</font></b></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80 height="16">
<font size="2">38-77</font></TD>
<TD align=center bgColor=#cffccd width=55 height="16">
<font size="2"><b>33</b></font></TD></font>
</tr>
</TBODY></TABLE>


'''

htmlstring19='''

<TABLE border=1 width="100%" cellpadding="0" cellspacing="0">
<TBODY>
<TR><TD align=center bgColor=#fcc2c8 width=35>
<p><font size="2">М</font></p></TD>
<TD align=middle bgColor=#fcc2c8 width=225>
<p style="margin-left: 3" align="left"><font size="2">Клуб</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=55>
<p><font size="2">Игр</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<p><font size="2">Победы</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<p><font size="2">Ничьи</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<p><font size="2">Пораж.</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<p><font size="2">Мячи</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=55>
<p><font size="2">Очки</font></p></TD></TR>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">1</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#FF0000">ЧЕЛСИ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">29</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">1</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">72-15</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>95</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
	<font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">2</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#000080">АРСЕНАЛ</font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">25</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">87-36</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>83</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">3</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#000080">МАНЧЕСТЕР ЮНАЙТЕД</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">22</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">58-26</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>77</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">4</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ЭВЕРТОН</font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-46</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>61</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">5</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ЛИВЕРПУЛЬ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">52-41</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>58</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">6</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">БОЛТОН</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">49-44</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>58</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">7</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">МИДДЛСБРО</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">53-46</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>55</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">8</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">МАНЧЕСТЕР СИТИ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">47-39</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>52</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">9</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ТОТТЕНХЭМ</font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">47-41</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>52</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">10</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">АСТОН ВИЛЛА</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-52</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>47</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">11</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ЧАРЛЬТОН</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">42-58</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>46</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">12</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">БИРМИНГЕМ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">40-46</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>45</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">13</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ФУЛХЭМ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">52-60</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>44</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">14</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">НЬЮКАСЛ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">47-57</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>44</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">15</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">БЛЭКБЕРН</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">32-43</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>42</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">16</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ПОРТСМУТ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">43-59</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>39</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">17</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b>ВЕСТ БРОМВИЧ</b></font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">36-61</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>34</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">18</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2" color="#800080"><b>КРИСТАЛ ПЭЛАС</b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">41-62</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>33</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">19</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2" color="#800080"><b>НОРВИЧ</b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">42-77</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>33</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">20</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#800080">САУТГЕМПТОН</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-66</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>32</b></font></TD></font>
	</font>
	</font>
</tr>
</TBODY></TABLE>
'''

htmlstring18='''

<TABLE border=1 width="100%" cellpadding="0" cellspacing="0" id="table6">
<TBODY>
<TR><TD align=center bgColor=#fcc2c8 width=35>
<font size="2">М</font></TD>
<TD align=middle bgColor=#fcc2c8 width=225>
<p style="margin-left: 3" align="left"><font size="2">Клуб</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=55>
<font size="2">Игр</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Победы</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Ничьи</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Пораж.</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Мячи</font></TD>
<TD align=center bgColor=#fcc2c8 width=55>
<font size="2">Очки</font></TD></TR>
<tr>
	<font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">1</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#FF0000">ЧЕЛСИ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">29</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">4</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">72-22</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>91</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">2</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">МАНЧЕСТЕР ЮНАЙТЕД</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">25</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">72-34</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>83</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">3</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ЛИВЕРПУЛЬ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">25</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">57-25</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>82</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
	<font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">4</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">АРСЕНАЛ</font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">68-31</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>67</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">5</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ТОТТЕНХЭМ</font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">53-38</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>65</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">6</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">БЛЭКБЕРН</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">51-42</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>63</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">7</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">НЬЮКАСЛ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">47-42</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>58</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">8</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">БОЛТОН</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">49-41</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>56</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">9</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b>ВЕСТ ХЭМ</b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">52-55</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>55</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">10</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b>УИГАН</b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-52</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>51</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">11</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ЭВЕРТОН</font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-49</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>50</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">12</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ФУЛХЭМ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">48-58</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>48</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">13</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ЧАРЛЬТОН</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">41-55</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>47</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">14</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">МИДДЛСБРО</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">48-58</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>45</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">15</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">МАНЧЕСТЕР СИТИ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">4</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">21</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">43-48</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>43</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">16</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">АСТОН ВИЛЛА</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">42-55</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>42</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">17</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2">ПОРТСМУТ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">37-62</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>38</b></font></TD></font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">18</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#800080">БИРМИНГЕМ</font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">28-50</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>34</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">19</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2" color="#800080"><b>ВЕСТ БРОМВИЧ</b></font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">22</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">31-58</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>30</b></font></TD></font>
</tr>
<tr>
  <font face="Arial">
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">20</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2" color="#800080"><b>САНДЕРЛЕНД</b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">3</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">29</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">26-69</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>15</b></font></TD></font>
	</font>
	</font>
</tr>
</TBODY></TABLE>

'''
htmlstring17='''
<TABLE border=1 width="100%" cellpadding="0" cellspacing="0" id="table6">
<TBODY>
<TR><TD align=center bgColor=#fcc2c8 width=35>
<font size="2">М</font></TD>
<TD align=middle bgColor=#fcc2c8 width=225>
<p style="margin-left: 3" align="left"><font size="2">Клуб</font></p></TD>
<TD align=center bgColor=#fcc2c8 width=55>
<font size="2">Игр</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Победы</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Ничьи</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Пораж.</font></TD>
<TD align=center bgColor=#fcc2c8 width=80>
<font size="2">Мячи</font></TD>
<TD align=center bgColor=#fcc2c8 width=55>
<font size="2">Очки</font></TD></TR>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">1</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#FF0000">
<a href="teams/manutd.htm"><font color="#FF0000">МАНЧЕСТЕР ЮНАЙТЕД</font></a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">28</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">83-27</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>89</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">2</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/chelsea.htm">
ЧЕЛСИ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">24</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">3</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">64-24</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>83</b></font></TD></font>
	</font>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">3</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/liverpool.htm">ЛИВЕРПУЛЬ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">57-27</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>68</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">4</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/arsenal.htm">
АРСЕНАЛ</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">63-35</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>68</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">5</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/tottenham.htm">
ТОТТЕНХЭМ</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">57-54</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>60</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">6</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/everton.htm">
ЭВЕРТОН</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">52-36</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>58</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">7</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/bolton.htm">БОЛТОН</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">47-52</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>56</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">8</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/reading.htm">РЕДИНГ</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">52-47</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>55</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">9</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/portsmouth.htm">
ПОРТСМУТ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-42</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>54</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">10</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#800080">
<a href="teams/blackburn.htm">БЛЭКБЕРН</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">52-54</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>52</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">11</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/aston%20villa.htm">АСТОН ВИЛЛА</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">43-41</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>50</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">12</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/middles.htm">МИДЛСБРО</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">44-49</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>46</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">13</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/newcastle.htm">
НЬЮКАСЛ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">38-47</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>43</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">14</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/mancity.htm">МАНЧЕСТЕР СИТИ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">29-44</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>42</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">15</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/west_ham.htm">
ВЕСТ ХЭМ</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">21</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">35-59</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>41</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">16</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/fulham.htm">ФУЛХЭМ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">38-60</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>39</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">17</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/wigan.htm">
УИГАН</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">37-59</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>38</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">18</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2" color="#800080"><b>
<a href="teams/sheff.htm"><font color="#800080">ШЕФФИЛД ЮНАЙТЕД</font></a></b></font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">32-55</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>38</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">19</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/charlton.htm">
<font color="#800080">ЧАРЛЬТОН</font></a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-60</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>34</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">20</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2" color="#800080"><b>
<a href="teams/watford.htm"><font color="#800080">УОТФОРД</font></a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">29-59</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>28</b></font></TD></font>
	</font>
	</tr>
</TBODY></TABLE>

'''

htmlstring16='''
<TABLE border=1 width="100%" cellpadding="0" cellspacing="0" id="table6">
<TBODY>
<TR><TD align=center bgColor=#F1F8E4 width=35>
<font size="2">М</font></TD>
<TD align=middle bgColor=#F1F8E4 width=225>
<p style="margin-left: 3" align="left"><font size="2">Клуб</font></p></TD>
<TD align=center bgColor=#F1F8E4 width=55>
<font size="2">И</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">В</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">Н</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">П</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">Мячи</font></TD>
<TD align=center bgColor=#F1F8E4 width=55>
<font size="2">Очки</font></TD></TR>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">1</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#FF0000">
<a href="teams/manutd.htm"><font color="#FF0000">МАНЧЕСТЕР ЮНАЙТЕД</font></a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">27</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">80-22</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>87</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">2</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/chelsea.htm">
ЧЕЛСИ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">25</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">3</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">65-26</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>85</b></font></TD></font>
	</font>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">3</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/arsenal.htm">
АРСЕНАЛ</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">24</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">3</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">74-31</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>83</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">4</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/liverpool.htm">
ЛИВЕРПУЛЬ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">21</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">4</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">67-28</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>76</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">5</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/everton.htm">
ЭВЕРТОН</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">55-33</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>65</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">6</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/aston%20villa.htm">АСТОН ВИЛЛА</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">71-51</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>60</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">7</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#800080">
<a href="teams/blackburn.htm">БЛЭКБЕРН</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">50-48</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>58</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">8</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/portsmouth.htm">
ПОРТСМУТ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">48-40</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>57</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">9</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/mancity.htm">
МАНЧЕСТЕР СИТИ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-53</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>55</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>



<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">10</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/west_ham.htm">
ВЕСТ ХЭМ</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">42-50</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>49</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">11</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/tottenham.htm">
ТОТТЕНХЭМ</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">66-61</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>46</b></font></TD>
</tr>

<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">12</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/newcastle.htm">
НЬЮКАСЛ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-65</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>43</b></font></TD></font>
	</font>
	</tr>

<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">13</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/middles.htm">
МИДЛСБРО</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">43-53</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>42</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>

<tr>


<TD align=center bgColor=#CFFCCD width=35>
<font size="2">14</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/wigan.htm">
УИГАН</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-51</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>40</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>

<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">15</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3">
<font size="2" color="#800080"><b><a href="teams/sunderland.htm">
САНДЕРЛЕНД</a></b></font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">21</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">36-59</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>39</b></font></TD>
</tr>

<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">16</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/bolton.htm">
БОЛТОН</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">36-54</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>37</b></font></TD></font>
	</font>
	</tr>

<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">17</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/fulham.htm">
ФУЛХЭМ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">38-60</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>36</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>

<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">18</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/reading.htm">
<font color="#800080">РЕДИНГ</font></a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">22</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">41-66</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>36</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>


<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">19</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3">
<font size="2" color="#800080"><b><a href="teams/birmingham.htm">
<font color="#800080">БИРМИНГЕМ</font></a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">46-62</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>35</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>

<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">20</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3">
<font size="2" color="#800080"><b><a href="teams/derby.htm">
<font color="#800080">ДЕРБИ</font></a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">1</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">29</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20-89</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>11</b></font></TD></font>
	</font>
	</tr>
</TBODY></TABLE>'''

htmlstring15='''
<TABLE border=1 width="100%" cellpadding="0" cellspacing="0" id="table6">
<TBODY>
<TR><TD align=center bgColor=#F1F8E4 width=35>
<font size="2">М</font></TD>
<TD align=middle bgColor=#F1F8E4 width=225>
<p style="margin-left: 3" align="left"><font size="2">Клуб</font></p></TD>
<TD align=center bgColor=#F1F8E4 width=55>
<font size="2">И</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">В</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">Н</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">П</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">Мячи</font></TD>
<TD align=center bgColor=#F1F8E4 width=55>
<font size="2">Очки</font></TD></TR>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">1</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#FF0000">
<a href="teams/manutd.htm"><font color="#FF0000">МАНЧЕСТЕР ЮНАЙТЕД</font></a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">28</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">4</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">68-24</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>90</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">2</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/liverpool.htm">
ЛИВЕРПУЛЬ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">25</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">2</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">77-27</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>86</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">3</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/chelsea.htm">
ЧЕЛСИ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">25</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">68-24</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>83</b></font></TD></font>
	</font>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">4</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/arsenal.htm">
АРСЕНАЛ</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">68-37</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>72</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">5</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/everton.htm">
ЭВЕРТОН</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">55-37</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>63</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">6</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/aston%20villa.htm">
АСТОН ВИЛЛА</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">54-48</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>62</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#FFFFCC width=35>
<font size="2">7</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/fulham.htm">
ФУЛХЭМ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">39-34</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>53</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">8</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/tottenham.htm">
ТОТТЕНХЭМ</a></font></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">45-45</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>51</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">9</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/west_ham.htm">
ВЕСТ ХЭМ</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">42-45</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>51</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">10</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/mancity.htm">
МАНЧЕСТЕР СИТИ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">15</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">58-50</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>50</b></font></TD></font>
	</font>
	</font>
	</font>
	</font>
	</font>
	</tr>
<tr>


<TD align=center bgColor=#CFFCCD width=35>
<font size="2">11</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/wigan.htm">
УИГАН</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-45</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>45</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">12</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3">
<font size="2" color="#800080"><b><a href="teams/stoke.htm">
СТОК СИТИ</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">38-55</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>45</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">13</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/bolton.htm">
БОЛТОН</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">41-53</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>41</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">14</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/portsmouth.htm">
ПОРТСМУТ</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">38-57</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>41</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">15</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2" color="#800080">
<a href="teams/blackburn.htm">БЛЭКБЕРН</a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">40-60</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>41</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">16</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3">
<font size="2" color="#800080"><b><a href="teams/sunderland.htm">
САНДЕРЛЕНД</a></b></font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-54</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>36</b></font></TD>
</tr>
<tr>
<TD align=center bgColor=#CFFCCD width=35>
<font size="2">17</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3">
<font size="2" color="#800080"><b><a href="teams/hull.htm">
ХАЛЛ СИТИ</a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">39-64</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>35</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">18</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/newcastle.htm">
<font color="#800080">НЬЮКАСЛ</font></a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">40-59</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>34</b></font></TD></font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">19</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><font size="2"><a href="teams/middles.htm">
<font color="#800080">МИДЛСБРО</font></a></font></b></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">28-57</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>32</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">20</font></TD>
  <font face="Arial" size="2">
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><font size="2"><b><a href="teams/wba.htm">
<font color="#800080">ВЕСТ БРОМВИЧ</font></a></b></font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
  <font face="Arial" size="2">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
  <font face="Arial">
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">22</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">36-67</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>32</b></font></TD></font>
	</font>
	</font>
	</font>
	</tr>
'''
htmlstring14='''


<TABLE border=1 width="100%" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#808080"><TBODY>
<TR><TD align=center bgColor=#F1F8E4 width=35>
<font size="2">М</font></TD>
<TD align=middle bgColor=#F1F8E4 width=225>
<p style="margin-left: 3" align="left"><font size="2">Клуб</font></p></TD>
<TD align=center bgColor=#F1F8E4 width=55>
<font size="2">И</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">В</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">Н</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">П</font></TD>
<TD align=center bgColor=#F1F8E4 width=80>
<font size="2">Мячи</font></TD>
<TD align=center bgColor=#F1F8E4 width=55>
<font size="2">Очки</font></TD></TR>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">1</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/chelsea.htm">
<font size="2" color="#FF0000">ЧЕЛСИ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">27</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">5</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">103-32</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>86</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">2</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/manutd.htm">
<font size="2">МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">27</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">4</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">86-28</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>85</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">3</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/arsenal.htm">
<font size="2">АРСЕНАЛ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">23</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">83-41</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>75</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">4</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/tottenham.htm">
<font size="2">ТОТТЕНХЭМ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">21</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">67-41</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>70</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#FFFFCC width=35>
<font size="2">5</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/mancity.htm">
<font size="2">МАНЧЕСТЕР СИТИ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">73-45</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>67</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#FFFFCC width=35>
<font size="2">6</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/aston%20villa.htm">
<font size="2">АСТОН ВИЛЛА</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">17</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">52-39</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>64</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#FFFFCC width=35>
<font size="2">7</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/liverpool.htm">
<font size="2">ЛИВЕРПУЛЬ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">61-35</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>63</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">8</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/everton.htm">
<font size="2">ЭВЕРТОН</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">60-49</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>61</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">9</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/birmingham.htm">
<font size="2">БИРМИНГЕМ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">38-47</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>50</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">10</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/blackburn.htm">
<font size="2">БЛЭКБЕРН</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">41-55</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>50</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">11</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/stoke.htm">
<font size="2">СТОК СИТИ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">14</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">13</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-48</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>47</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">12</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/fulham.htm">
<font size="2">ФУЛХЭМ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">39-46</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>46</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">13</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/sunderland.htm">
<font size="2">САНДЕРЛЕНД</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">16</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">48-56</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>44</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">14</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/bolton.htm">
<font size="2">БОЛТОН</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">10</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">42-67</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>39</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">15</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/wolves.htm">
<font size="2">ВУЛВЕРХЭМПТОН</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">18</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">32-56</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>38</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">16</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/wigan.htm">
<font size="2">УИГАН</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">9</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">37-79</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>36</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#CFFCCD width=35>
<font size="2">17</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/west_ham.htm">
<font size="2">ВЕСТ ХЭМ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">11</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">19</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">47-66</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>35</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">18</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/burnley.htm">
<font size="2" color="#800080">БЕРНЛИ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">8</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">24</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">42-82</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>30</b></font></TD>
</font>
</tr>
<tr>

<font face="Arial">

<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">19</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/hull.htm">
<font size="2" color="#800080">ХАЛЛ СИТИ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">6</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">12</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">20</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-75</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>30</b></font></TD>
</font>
</tr>
<tr>
<TD align=center bgColor=#E2E7E4 width=35>
<font size="2">20</font></TD>
<TD bgColor=#cffccd width=225>
<p style="margin-left: 3"><b><a href="teams/portsmouth.htm">
<font size="2" color="#800080">ПОРТСМУТ</font></a></b></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2">38</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">7</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">24</font></TD>
<TD align=center bgColor=#cffccd width=80>
<font size="2">34-66</font></TD>
<TD align=center bgColor=#cffccd width=55>
<font size="2"><b>19</b></font></TD>
</tr>

</TBODY></TABLE>

'''

htmlstring13='''
 <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=middle bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/manutd.htm'><font size=2 color=#FF0000>&nbsp;МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>4</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>78-37</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>80</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/chelsea.htm'><font size=2>&nbsp;ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>69-33</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>71</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/mancity.htm'><font size=2>&nbsp;МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>60-33</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>71</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/arsenal.htm'><font size=2>&nbsp;АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>72-43</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>68</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/tottenham.htm'><font size=2>&nbsp;ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>55-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>62</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>6</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/liverpool.htm'><font size=2>&nbsp;ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>59-44</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>58</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>7</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/everton.htm'><font size=2>&nbsp;ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>51-45</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>54</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/fulham.htm'><font size=2>&nbsp;ФУЛХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>49-43</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>49</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/astonvilla.htm'><font size=2>&nbsp;АСТОН ВИЛЛА</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-59</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>48</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/Sunderland.htm'><font size=2>&nbsp;САНДЕРЛЕНД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/westbrom.htm'><font size=2>&nbsp;ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>56-71</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/newcastle.htm'><font size=2>&nbsp;НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>56-57</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/stoke.htm'><font size=2>&nbsp;СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>46-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/bolton.htm'><font size=2>&nbsp;БОЛТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>52-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/blackburn.htm'><font size=2>&nbsp;БЛЭКБЕРН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>46-59</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>43</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/wigan.htm'><font size=2>&nbsp;УИГАН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-61</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>42</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/wolves.htm'><font size=2>&nbsp;ВУЛВЕРХЭМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>46-66</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/birmingham.htm'><font size=2 color=#800080>&nbsp;БИРМИНГЕМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>37-58</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/blackpool.htm'><font size=2 color=#800080>&nbsp;БЛЭКПУЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>55-78</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2011/teams/west_ham.htm'><font size=2 color=#800080>&nbsp;ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-70</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>33</b></font></td>
  </tr>
  </TBODY>
</TABLE>
'''

htmlstring12='''
<TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=middle bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/mancity.htm'><font size=2 color=#FF0000>&nbsp;МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>93-29</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>89</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/manutd.htm'><font size=2>&nbsp;МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>89-33</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>89</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/arsenal.htm'><font size=2>&nbsp;АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>74-49</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>70</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>4</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/tottenham.htm'><font size=2>&nbsp;ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>66-41</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>69</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/newcastle.htm'><font size=2>&nbsp;НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>56-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>65</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>6</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/chelsea.htm'><font size=2>&nbsp;ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>65-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>64</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>7</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/everton.htm'><font size=2>&nbsp;ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>50-40</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>56</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>8</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/liverpool.htm'><font size=2>&nbsp;ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-40</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>52</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/fulham.htm'><font size=2>&nbsp;ФУЛХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>52</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/westbrom.htm'><font size=2>&nbsp;ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-52</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/swansea.htm'><font size=2>&nbsp;СУОНСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>44-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/norwich.htm'><font size=2>&nbsp;НОРВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>52-66</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/Sunderland.htm'><font size=2>&nbsp;САНДЕРЛЕНД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/stoke.htm'><font size=2>&nbsp;СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>36-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/wigan.htm'><font size=2>&nbsp;УИГАН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>42-62</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>43</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/astonvilla.htm'><font size=2>&nbsp;АСТОН ВИЛЛА</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>37-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>38</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/qpr.htm'><font size=2>&nbsp;КПР</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-66</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>37</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/bolton.htm'><font size=2 color=#800080>&nbsp;БОЛТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>46-77</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>36</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/blackburn.htm'><font size=2 color=#800080>&nbsp;БЛЭКБЕРН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-78</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>31</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td bgcolor=#cffccd width=225><b><a href='/england/2012/teams/wolves.htm'><font size=2 color=#800080>&nbsp;ВУЛВЕРХЭМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-82</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>25</b></font></td>
  </tr>
  </TBODY>
</TABLE>

'''


htmlstring11='''

 <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=middle bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2013/teams/manutd.htm'>МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>86-43</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>89</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/mancity.htm'>МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>66-34</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>78</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/chelsea.htm'>ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>75-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>75</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/arsenal.htm'>АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>72-37</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>73</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/tottenham.htm'>ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>66-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>72</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>6</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/everton.htm'>ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>55-40</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>63</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>7</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/liverpool.htm'>ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>71-43</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>61</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/westbrom.htm'>ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>53-57</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>49</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>9</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/swansea.htm'>СУОНСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/west_ham.htm'>ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/norwich.htm'>НОРВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-58</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/fulham.htm'>ФУЛХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>50-60</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>43</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/stoke.htm'>СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>34-45</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>42</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/southampton.htm'>САУТГЕМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>49-60</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/astonvilla.htm'>АСТОН ВИЛЛА</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-69</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/newcastle.htm'>НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-68</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2013/teams/Sunderland.htm'>САНДЕРЛЕНД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2013/teams/wigan.htm'>УИГАН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-73</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>36</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2013/teams/reading.htm'>РЕДИНГ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-73</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>28</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2013/teams/qpr.htm'>КПР</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>4</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>30-60</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>25</b></font></td>
  </tr>
  </TBODY>
</TABLE>
'''

htmlstring10='''


  <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=middle bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2014/teams/mancity.htm'>МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>102-37</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>86</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/liverpool.htm'>ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>101-50</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>84</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/chelsea.htm'>ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>25</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>71-27</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>82</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/arsenal.htm'>АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>24</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>68-41</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>79</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/everton.htm'>ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>61-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>72</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/tottenham.htm'>ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>55-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>69</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>7</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/manutd.htm'>МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>64-43</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>64</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/southampton.htm'>САУТГЕМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>54-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>56</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/stoke.htm'>СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-52</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>50</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/newcastle.htm'>НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>4</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-59</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>49</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/crystalpalace.htm'>КРИСТАЛ ПЭЛАС</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>33-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/swansea.htm'>СУОНСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>54-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>42</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/west_ham.htm'>ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/Sunderland.htm'>САНДЕРЛЕНД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-60</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>38</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/astonvilla.htm'>АСТОН ВИЛЛА</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>39-61</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>38</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>16</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/hull.htm'>ХАЛЛ СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>38-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>37</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2014/teams/westbrom.htm'>ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-59</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>36</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2014/teams/norwich.htm'>НОРВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28-62</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>33</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2014/teams/fulham.htm'>ФУЛХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>24</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-85</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>32</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2014/teams/cardiff.htm'>КАРДИФФ СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>32-74</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>30</b></font></td>
  </tr>
  </TBODY>
</TABLE>

'''

htmlstring9='''
  <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2015/teams/chelsea.htm'>ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>73-32</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>87</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/mancity.htm'>МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>24</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>83-38</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>79</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/arsenal.htm'>АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>71-36</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>75</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/manutd.htm'>МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>62-37</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>70</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/tottenham.htm'>ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>58-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>64</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/liverpool.htm'>ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>52-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>62</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/southampton.htm'>САУТГЕМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>54-33</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>60</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/swansea.htm'>СУОНСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>46-49</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>56</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/stoke.htm'>СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-45</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>54</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/crystalpalace.htm'>КРИСТАЛ ПЭЛАС</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>48</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/everton.htm'>ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-50</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/west_ham.htm'>ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>44-47</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/westbrom.htm'>ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>38-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/leicester.htm'>ЛЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>46-55</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/newcastle.htm'>НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-63</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/Sunderland.htm'>САНДЕРЛЕНД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>31-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>38</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2015/teams/astonvilla.htm'>АСТОН ВИЛЛА</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>31-57</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>38</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2015/teams/hull.htm'>ХАЛЛ СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>33-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>35</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2015/teams/burnley.htm'>БЕРНЛИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>33</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2015/teams/qpr.htm'>КПР</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>24</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>42-73</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>30</b></font></td>
  </tr>
  </TBODY>
</TABLE>

'''
htmlstring8='''
 <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2016/teams/leicester.htm'>ЛЕСТЕР</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>68-36</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>81</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/arsenal.htm'>АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>65-36</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>71</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/tottenham.htm'>ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>69-35</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>70</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/mancity.htm'>МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>71-41</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>66</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/manutd.htm'>МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>49-35</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>66</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/southampton.htm'>САУТГЕМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>59-41</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>63</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/west_ham.htm'>ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>65-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>62</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/liverpool.htm'>ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>63-50</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>60</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/stoke.htm'>СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-55</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>51</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/chelsea.htm'>ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>59-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>50</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/everton.htm'>ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>59-55</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/swansea.htm'>СУОНСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>42-52</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/watford.htm'>УОТФОРД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-50</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/westbrom.htm'>ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>34-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>43</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/crystalpalace.htm'>КРИСТАЛ ПЭЛАС</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>39-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>42</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/bournemouth.htm'>БОРНМУТ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-67</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>42</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2016/teams/Sunderland.htm'>САНДЕРЛЕНД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-62</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2016/teams/newcastle.htm'>НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>44-65</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>37</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2016/teams/norwich.htm'>НОРВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>39-67</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>34</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2016/teams/astonvilla.htm'>АСТОН ВИЛЛА</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27-76</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>17</b></font></td>
  </tr>
  </TBODY>
</TABLE>


'''

htmlstring7='''
  <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2017/teams/chelsea.htm'>ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>30</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>85-33</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>93</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/tottenham.htm'>ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>4</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>86-26</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>86</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/mancity.htm'>МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>80-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>78</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/liverpool.htm'>ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>78-42</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>76</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/arsenal.htm'>АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>77-44</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>75</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/manutd.htm'>МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>54-29</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>69</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/everton.htm'>ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>62-44</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>61</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/southampton.htm'>САУТГЕМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/bournemouth.htm'>БОРНМУТ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>55-67</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/westbrom.htm'>ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/west_ham.htm'>ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-64</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/leicester.htm'>ЛЕСТЕР</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-63</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/stoke.htm'>СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/crystalpalace.htm'>КРИСТАЛ ПЭЛАС</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>50-63</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/swansea.htm'>СУОНСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-70</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/burnley.htm'>БЕРНЛИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>39-55</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2017/teams/watford.htm'>УОТФОРД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-68</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2017/teams/hull.htm'>ХАЛЛ СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>37-80</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>34</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2017/teams/middlesbrough.htm'>МИДЛСБРО</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>28</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2017/teams/Sunderland.htm'>САНДЕРЛЕНД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>29-69</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>24</b></font></td>
  </tr>
  </TBODY>
</TABLE>
'''

htmlstring6='''
 <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2018/teams/mancity.htm'>МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>32</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>4</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>2</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>106-27</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>100</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/manutd.htm'>МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>25</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>68-28</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>81</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/tottenham.htm'>ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>74-36</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>77</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/liverpool.htm'>ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>84-38</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>75</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/chelsea.htm'>ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>62-38</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>70</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/arsenal.htm'>АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>74-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>63</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/burnley.htm'>БЕРНЛИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>36-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>54</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/everton.htm'>ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>44-58</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>49</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/leicester.htm'>ЛЕСТЕР</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>56-60</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>47</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/newcastle.htm'>НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>39-47</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/crystalpalace.htm'>КРИСТАЛ ПЭЛАС</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-55</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/bournemouth.htm'>БОРНМУТ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-61</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/west_ham.htm'>ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-68</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>42</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/watford.htm'>УОТФОРД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>44-64</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/brighton.htm'>БРАЙТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>34-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/huddersfield.htm'>ХАДДЕРСФИЛД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28-58</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>37</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2018/teams/southampton.htm'>САУТГЕМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>37-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>36</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2018/teams/swansea.htm'>СУОНСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>33</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2018/teams/stoke.htm'>СТОК СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>35-68</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>33</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2018/teams/westbrom.htm'>ВЕСТ БРОМВИЧ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>31-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>31</b></font></td>
  </tr>
  </TBODY>
</TABLE>

'''

htmlstring5='''


  <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2019/teams/mancity.htm'>МАНЧЕСТЕР СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>32</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>2</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>4</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>95-23</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>98</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/liverpool.htm'>ЛИВЕРПУЛЬ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>30</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>1</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>89-22</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>97</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/chelsea.htm'>ЧЕЛСИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>63-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>72</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/tottenham.htm'>ТОТТЕНХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>2</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>67-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>71</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/arsenal.htm'>АРСЕНАЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>73-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>70</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/manutd.htm'>МАНЧЕСТЕР ЮНАЙТЕД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>65-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>66</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/wolves.htm'>ВУЛВЕРХЭМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>57</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/everton.htm'>ЭВЕРТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>54-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>54</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/leicester.htm'>ЛЕСТЕР</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>51-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>52</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/west_ham.htm'>ВЕСТ ХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>52-55</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>52</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/watford.htm'>УОТФОРД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>52-59</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>50</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/crystalpalace.htm'>КРИСТАЛ ПЭЛАС</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>51-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>49</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/newcastle.htm'>НЬЮКАСЛ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>42-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/bournemouth.htm'>БОРНМУТ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>56-70</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/burnley.htm'>БЕРНЛИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-68</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/southampton.htm'>САУТГЕМПТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>45-65</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2019/teams/brighton.htm'>БРАЙТОН</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>35-60</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>36</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2019/teams/cardiff.htm'>КАРДИФФ СИТИ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>4</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>24</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>34-69</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>34</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2019/teams/fulham.htm'>ФУЛХЭМ</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>34-81</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>26</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2019/teams/huddersfield.htm'>ХАДДЕРСФИЛД</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22-76</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>16</b></font></td>
  </tr>
  </TBODY>
</TABLE>
'''

htmlstring4='''
  <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2020/teams/liverpool.htm'>Ливерпуль</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>32</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>85-33</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>99</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/mancity.htm'>Манчестер Сити</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>102-35</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>81</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/manutd.htm'>Манчестер Юнайтед</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>66-36</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>66</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/chelsea.htm'>Челси</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>69-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>66</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/leicester.htm'>Лестер</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>67-41</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>62</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/tottenham.htm'>Тоттенхэм</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>61-47</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>59</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/wolves.htm'>Вулверхэмптон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>51-40</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>59</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/arsenal.htm'>Арсенал</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>56-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>56</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/sheffutd.htm'>Шеффилд Юнайтед</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>39-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>54</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/burnley.htm'>Бернли</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-50</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>54</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/southampton.htm'>Саутгемптон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>51-60</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>52</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/everton.htm'>Эвертон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>44-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>49</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/newcastle.htm'>Ньюкасл</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>38-58</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/crystalpalace.htm'>Кристал Пэлас</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>31-50</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>43</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/brighton.htm'>Брайтон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>39-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/west_ham.htm'>Вест Хэм</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>49-62</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2020/teams/astonvilla.htm'>Астон Вилла</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-67</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>35</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2020/teams/bournemouth.htm'>Борнмут</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-65</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>34</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2020/teams/watford.htm'>Уотфорд</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>36-64</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>34</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2020/teams/norwich.htm'>Норвич</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26-75</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>21</b></font></td>
  </tr>
  </TBODY>
</TABLE>
'''

htmlstring3='''

  <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2021/teams/mancity.htm'>Манчестер Сити</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>83-32</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>86</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/manutd.htm'>Манчестер Юнайтед</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>73-44</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>74</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/liverpool.htm'>Ливерпуль</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>68-42</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>69</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/chelsea.htm'>Челси</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>58-36</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>67</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/leicester.htm'>Лестер</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>68-50</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>66</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/west_ham.htm'>Вест Хэм</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>62-47</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>65</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/tottenham.htm'>Тоттенхэм</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>68-45</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>62</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/arsenal.htm'>Арсенал</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>55-39</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>61</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/leeds.htm'>Лидс</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>62-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>59</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/everton.htm'>Эвертон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>59</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/astonvilla.htm'>Астон Вилла</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>55-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>55</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/newcastle.htm'>Ньюкасл</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>46-62</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/wolves.htm'>Вулверхэмптон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>36-52</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/crystalpalace.htm'>Кристал Пэлас</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>41-66</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/southampton.htm'>Саутгемптон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>47-68</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>43</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/brighton.htm'>Брайтон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>40-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2021/teams/burnley.htm'>Бернли</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>33-55</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2021/teams/fulham.htm'>Фулхэм</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>28</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2021/teams/westbrom.htm'>Вест Бромвич</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>35-76</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>26</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2021/teams/sheffutd.htm'>Шеффилд Юнайтед</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>2</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>29</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>20-63</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>23</b></font></td>
  </tr>
  </TBODY>
</TABLE>
'''
htmlstring2='''


 <TBODY> 
  <TR> 
    <TD align=center bgColor=#F1F8E4 
width=35><FONT size=2 face="Arial">М</FONT></TD>
    <TD align=left bgColor=#F1F8E4 
width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><font size="2">И</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">В</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">Н</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><font size="2">П</font></TD>
    <TD align=center bgColor=#F1F8E4 
width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
    <TD align=center bgColor=#F1F8E4 
width=55><FONT size=2 face="Arial">Очки</FONT></TD>
  </TR>	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2022/teams/mancity.htm'>Манчестер Сити</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>29</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>99-26</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>93</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/liverpool.htm'>Ливерпуль</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>28</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>2</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>94-26</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>92</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/chelsea.htm'>Челси</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>76-33</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>74</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/tottenham.htm'>Тоттенхэм</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>69-40</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>71</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/arsenal.htm'>Арсенал</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>3</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>61-48</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>69</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/manutd.htm'>Манчестер Юнайтед</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>57-57</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>58</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/west_ham.htm'>Вест Хэм</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>60-51</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>56</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/leicester.htm'>Лестер</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>62-59</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>52</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/brighton.htm'>Брайтон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>42-44</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>51</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/wolves.htm'>Вулверхэмптон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>38-43</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>51</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/newcastle.htm'>Ньюкасл</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>44-62</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>49</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/crystalpalace.htm'>Кристал Пэлас</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>50-46</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>48</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/brentford.htm'>Брентфорд</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>48-56</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>46</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>14</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/astonvilla.htm'>Астон Вилла</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>52-54</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/southampton.htm'>Саутгемптон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-67</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/everton.htm'>Эвертон</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>43-66</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2022/teams/leeds.htm'>Лидс</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>42-79</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>38</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2022/teams/burnley.htm'>Бернли</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>17</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>34-53</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>35</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2022/teams/watford.htm'>Уотфорд</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>27</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>34-77</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>23</b></font></td>
  </tr>
	<tr>
    <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
    <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2022/teams/norwich.htm'>Норвич</font></a></b></td>
    <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
    <td align=center bgcolor=#cffccd width=80><font size=2>23-84</font></td>
    <td align=center bgcolor=#cffccd width=55><font size=2><b>22</b></font></td>
  </tr>
  </TBODY>
</TABLE>




'''


htmlstring1='''
    <TBODY> 
    <TR> 
      <TD align=center bgColor=#F1F8E4 
  width=35><FONT size=2 face="Arial">М</FONT></TD>
      <TD align=left bgColor=#F1F8E4 
  width=225><FONT size=2 face="Arial">&nbsp;Клуб</FONT></TD>
      <TD align=center bgColor=#F1F8E4 
  width=55><font size="2">И</font></TD>
      <TD align=center bgColor=#F1F8E4 
  width=80><font size="2">В</font></TD>
      <TD align=center bgColor=#F1F8E4 
  width=80><font size="2">Н</font></TD>
      <TD align=center bgColor=#F1F8E4 
  width=80><font size="2">П</font></TD>
      <TD align=center bgColor=#F1F8E4 
  width=80><FONT size=2 face="Arial">Мячи</FONT></TD>
      <TD align=center bgColor=#F1F8E4 
  width=55><FONT size=2 face="Arial">Очки</FONT></TD>
    </TR>	<tr>
      <td align=center bgcolor=#E2E7E4 width=35><font size=2>1</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#FF0000>&nbsp;<a href='/england/2023/teams/mancity.htm'>Манчестер Сити</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>28</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>94-33</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>89</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#E2E7E4 width=35><font size=2>2</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/arsenal.htm'>Арсенал</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>26</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>88-43</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>84</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#E2E7E4 width=35><font size=2>3</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/manutd.htm'>Манчестер Юнайтед</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>23</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>58-43</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>75</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#E2E7E4 width=35><font size=2>4</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/newcastle.htm'>Ньюкасл</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>5</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>68-33</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>71</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#FFFFCC width=35><font size=2>5</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/liverpool.htm'>Ливерпуль</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>75-47</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>67</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#FFFFCC width=35><font size=2>6</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/brighton.htm'>Брайтон</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>72-53</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>62</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#FFFFCC width=35><font size=2>7</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/astonvilla.htm'>Астон Вилла</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>13</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>51-46</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>61</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>8</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/tottenham.htm'>Тоттенхэм</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>70-63</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>60</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>9</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/brentford.htm'>Брентфорд</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>14</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>58-46</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>59</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>10</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/fulham.htm'>Фулхэм</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>55-53</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>52</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>11</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/crystalpalace.htm'>Кристал Пэлас</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>15</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>40-49</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>45</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>12</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/chelsea.htm'>Челси</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>16</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>38-47</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>44</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>13</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/wolves.htm'>Вулверхэмптон</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>19</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>31-58</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>41</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#FFFFCC width=35><font size=2>14</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/west_ham.htm'>Вест Хэм</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>20</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>42-55</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>40</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>15</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/bournemouth.htm'>Борнмут</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>37-71</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>39</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>16</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/nottingham_forest.htm'>Ноттингем Форест</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>11</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>38-68</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>38</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#CFFCCD width=35><font size=2>17</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2>&nbsp;<a href='/england/2023/teams/everton.htm'>Эвертон</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>8</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>12</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>18</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>34-57</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>36</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#E2E7E4 width=35><font size=2>18</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2023/teams/leicester.htm'>Лестер</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>9</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>22</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>51-68</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>34</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#E2E7E4 width=35><font size=2>19</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2023/teams/leeds.htm'>Лидс</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>10</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>21</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>48-78</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>31</b></font></td>
    </tr>
    <tr>
      <td align=center bgcolor=#E2E7E4 width=35><font size=2>20</font></td>
      <td align=left bgcolor=#cffccd width=225><b><font size=2 color=#800080>&nbsp;<a href='/england/2023/teams/southampton.htm'>Саутгемптон</font></a></b></td>
      <td align=center bgcolor=#cffccd width=55><font size=2>38</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>6</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>7</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>25</font></td>
      <td align=center bgcolor=#cffccd width=80><font size=2>36-73</font></td>
      <td align=center bgcolor=#cffccd width=55><font size=2><b>25</b></font></td>
    </tr>
    </TBODY>
  </TABLE>


'''

x1=szn2000_2001.season(htmlstring23)
x2=szn2001_2002.season(htmlstring22)
x3=szn2002_2003.season(htmlstring21)
x4=szn2003_2004.season(htmlstring20)
x5=szn2004_2005.season(htmlstring19)
x6=szn2005_2006.season(htmlstring18)
x7=szn2006_2007.season(htmlstring17)
x8=szn2007_2008.season(htmlstring16)
x9=szn2008_2009.season(htmlstring15)
x10=szn2009_2010.season(htmlstring14)
x11=szn2010_2011.season(htmlstring13)
x12=szn2011_2012.season(htmlstring12)
x13=szn2012_2013.season(htmlstring11)
x14=szn2013_2014.season(htmlstring10)
x15=szn2014_2015.season(htmlstring9)
x16=szn2015_2016.season(htmlstring8)
x17=szn2016_2017.season(htmlstring7)
x18=szn2017_2018.season(htmlstring6)
x19=szn2018_2019.season(htmlstring5)
x20=szn2019_2020.season(htmlstring4)
x21=szn2020_2021.season(htmlstring3)
x22=szn2021_2022.season(htmlstring2)
x23=szn2022_2023.season(htmlstring1)


# Подключение к базе данных
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="developer",
    password="1562473890Abc_",
    database="epl"
)

cursor = conn.cursor()


query1 = """
SELECT TeamName, SUM(Loses) AS count_of_loses
FROM (
    SELECT TeamName, Loses FROM season2000_2001
    UNION ALL
    SELECT TeamName, Loses FROM season2001_2002
    UNION ALL
    SELECT TeamName, Loses FROM season2002_2003
    UNION ALL
    SELECT TeamName, Loses FROM season2003_2004
    UNION ALL
    SELECT TeamName, Loses FROM season2004_2005
    UNION ALL
    SELECT TeamName, Loses FROM season2005_2006
    UNION ALL
    SELECT TeamName, Loses FROM season2006_2007
    UNION ALL
    SELECT TeamName, Loses FROM season2007_2008
    UNION ALL
    SELECT TeamName, Loses FROM season2008_2009
    UNION ALL
    SELECT TeamName, Loses FROM season2009_2010
    UNION ALL
    SELECT TeamName, Loses FROM season2010_2011
    UNION ALL
    SELECT TeamName, Loses FROM season2011_2012
    UNION ALL
    SELECT TeamName, Loses FROM season2012_2013
    UNION ALL
    SELECT TeamName, Loses FROM season2013_2014
    UNION ALL
    SELECT TeamName, Loses FROM season2014_2015
    UNION ALL
    SELECT TeamName, Loses FROM season2015_2016
    UNION ALL
    SELECT TeamName, Loses FROM season2016_2017
    UNION ALL
    SELECT TeamName, Loses FROM season2017_2018
    UNION ALL
    SELECT TeamName, Loses FROM season2018_2019
    UNION ALL
    SELECT TeamName, Loses FROM season2019_2020
    UNION ALL
    SELECT TeamName, Loses FROM season2020_2021
    UNION ALL
    SELECT TeamName, Loses FROM season2021_2022
    UNION ALL
    SELECT TeamName, Loses FROM season2022_2023
) AS combined_seasons
GROUP BY TeamName
ORDER BY count_of_loses DESC
LIMIT 1;
"""

query2 = '''
SELECT SUM(Goals) AS total_goals
FROM (
    SELECT Goals FROM season2000_2001
    UNION ALL
    SELECT Goals FROM season2001_2002
    UNION ALL
    SELECT Goals FROM season2002_2003
    UNION ALL
    SELECT Goals FROM season2003_2004
    UNION ALL
    SELECT Goals FROM season2004_2005
    UNION ALL
    SELECT Goals FROM season2005_2006
    UNION ALL
    SELECT Goals FROM season2006_2007
    UNION ALL
    SELECT Goals FROM season2007_2008
    UNION ALL
    SELECT Goals FROM season2008_2009
    UNION ALL
    SELECT Goals FROM season2009_2010
    UNION ALL
    SELECT Goals FROM season2010_2011
    UNION ALL
    SELECT Goals FROM season2011_2012
    UNION ALL
    SELECT Goals FROM season2012_2013
    UNION ALL
    SELECT Goals FROM season2013_2014
    UNION ALL
    SELECT Goals FROM season2014_2015
    UNION ALL
    SELECT Goals FROM season2015_2016
    UNION ALL
    SELECT Goals FROM season2016_2017
    UNION ALL
    SELECT Goals FROM season2017_2018
    UNION ALL
    SELECT Goals FROM season2018_2019
    UNION ALL
    SELECT Goals FROM season2019_2020
    UNION ALL
    SELECT Goals FROM season2020_2021
    UNION ALL
    SELECT Goals FROM season2021_2022
    UNION ALL
    SELECT Goals FROM season2022_2023
) AS combined_seasons
'''

'''
with average as
(
select 

)

'''


try:
    cursor.execute(query1)
    rows1 = cursor.fetchall()
    for row in rows1:
        print(row)

    cursor.execute(query2)
    row2 = cursor.fetchone()
    print(row2)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()




fig, axs = plt.subplots(8, 3, figsize=(18, 12))

axs[0, 0].bar(x1[0], x1[1], color='r', label='Winner')
axs[0, 0].set_xlabel('Team')
axs[0, 0].set_ylabel('Points')
axs[0, 0].set_title('Plot 1: Winner of the season 2000_2001')
axs[0, 0].legend()

axs[0, 1].bar(x2[0], x2[1], color='b', label='Winner')
axs[0, 1].set_xlabel('Team')
axs[0, 1].set_ylabel('Points')
axs[0, 1].set_title('Plot 2: Winner of the season 2001_2002')
axs[0, 1].legend()

axs[0, 2].bar(x3[0], x3[1], color='g', label='Winner')
axs[0, 2].set_xlabel('Team')
axs[0, 2].set_ylabel('Points')
axs[0, 2].set_title('Plot 3: Winner of the season 2002_2003')
axs[0, 2].legend()

axs[1, 0].bar(x4[0], x4[1], color='y', label='Winner')
axs[1, 0].set_xlabel('Team')
axs[1, 0].set_ylabel('Points')
axs[1, 0].set_title('Plot 4: Winner of the season 2003_2004')
axs[1, 0].legend()

axs[1, 1].bar(x5[0],x5[1], color='c', label='Winner')
axs[1, 1].set_xlabel('Team')
axs[1, 1].set_ylabel('Points')
axs[1, 1].set_title('Plot 5: Winner of the season 2004_2005')
axs[1, 1].legend()

axs[1, 2].bar(x6[0],x6[1], color='k', label='Winner')
axs[1, 2].set_xlabel('Team')
axs[1, 2].set_ylabel('Points')
axs[1, 2].set_title('Plot 6: Winner of the season 2005_2006')
axs[1, 2].legend()

axs[2, 0].bar(x7[0],x7[1], color='g', label='Winner')
axs[2,0].set_xlabel('Team')
axs[2,0].set_ylabel('Points')
axs[2,0].set_title('Plot 7: Winner of the season 2006_2007')
axs[2,0].legend()

axs[2, 1].bar(x8[0],x8[1], color='b', label='Winner')
axs[2,1].set_xlabel('Team')
axs[2,1].set_ylabel('Points')
axs[2,1].set_title('Plot 8: Winner of the season 2007_2008')
axs[2,1].legend()

axs[2,2].bar(x9[0],x9[1], color='y', label='Winner')
axs[2,2].set_xlabel('Team')
axs[2,2].set_ylabel('Points')
axs[2,2].set_title('Plot 9: Winner of the season 2008_2009')
axs[2,2].legend()

axs[3,0].bar(x10[0],x10[1], color='c', label='Winner')
axs[3,0].set_xlabel('Team')
axs[3,0].set_ylabel('Points')
axs[3,0].set_title('Plot 10: Winner of the season 2009_2010')
axs[3,0].legend()

axs[3,1].bar(x11[0],x11[1], color='k', label='Winner')
axs[3,1].set_xlabel('Team')
axs[3,1].set_ylabel('Points')
axs[3,1].set_title('Plot 11: Winner of the season 2010_2011')
axs[3,1].legend()

axs[3,2].bar(x12[0],x12[1], color='r', label='Winner')
axs[3,2].set_xlabel('Team')
axs[3,2].set_ylabel('Points')
axs[3,2].set_title('Plot 12: Winner of the season 2011_2012')
axs[3,2].legend()

axs[4,0].bar(x13[0],x13[1], color='g', label='Winner')
axs[4,0].set_xlabel('Team')
axs[4,0].set_ylabel('Points')
axs[4,0].set_title('Plot 13: Winner of the season 2012_2013')
axs[4,0].legend()

axs[4,1].bar(x14[0],x14[1], color='k', label='Winner')
axs[4,1].set_xlabel('Team')
axs[4,1].set_ylabel('Points')
axs[4,1].set_title('Plot 14: Winner of the season 2013_2014')
axs[4,1].legend()

axs[4,2].bar(x15[0],x15[1], color='m', label='Winner')
axs[4,2].set_xlabel('Team')
axs[4,2].set_ylabel('Points')
axs[4,2].set_title('Plot 15: Winner of the season 2014_2015')
axs[4,2].legend()

axs[5,0].bar(x16[0],x16[1], color='y', label='Winner')
axs[5,0].set_xlabel('Team')
axs[5,0].set_ylabel('Points')
axs[5,0].set_title('Plot 16: Winner of the season 2015_2016')
axs[5,0].legend()


axs[5,1].bar(x17[0],x17[1], color='r', label='Winner')
axs[5,1].set_xlabel('Team')
axs[5,1].set_ylabel('Points')
axs[5,1].set_title('Plot 17: Winner of the season 2016_2017')
axs[5,1].legend()


axs[5,2].bar(x18[0],x18[1], color='b', label='Winner')
axs[5,2].set_xlabel('Team')
axs[5,2].set_ylabel('Points')
axs[5,2].set_title('Plot 18: Winner of the season 2017_2018')
axs[5,2].legend()


axs[6,0].bar(x19[0],x19[1], color='g', label='Winner')
axs[6,0].set_xlabel('Team')
axs[6,0].set_ylabel('Points')
axs[6,0].set_title('Plot 19: Winner of the season 2018_2019')
axs[6,0].legend()

axs[6,1].bar(x20[0],x20[1], color='k', label='Winner')
axs[6,1].set_xlabel('Team')
axs[6,1].set_ylabel('Points')
axs[6,1].set_title('Plot 20: Winner of the season 2019_2020')
axs[6,1].legend()

axs[6,2].bar(x21[0],x21[1], color='c', label='Winner')
axs[6,2].set_xlabel('Team')
axs[6,2].set_ylabel('Points')
axs[6,2].set_title('Plot 21: Winner of the season 2020_2021')
axs[6,2].legend()

axs[7,0].bar(x22[0],x22[1], color='m', label='Winner')
axs[7,0].set_xlabel('Team')
axs[7,0].set_ylabel('Points')
axs[7,0].set_title('Plot 22: Winner of the season 2021_2022')
axs[7,0].legend()

axs[7,1].bar(x23[0],x23[1], color='k', label='Winner')
axs[7,1].set_xlabel('Team')
axs[7,1].set_ylabel('Points')
axs[7,1].set_title('Plot 23: Winner of the season 2022_2023')
axs[7,1].legend()

fig.delaxes(axs[7, 2])

plt.tight_layout()
plt.show()