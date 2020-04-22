
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" >
<html >

  <head >

    <TITLE > Peg Solitaire Online - Patience game < /TITLE >

    <meta content = "text/html; charset=utf-8" http-equiv = "content-type" >

    <meta name = "keywords"
          content = "Peg,Solitaire,Brainvita,Patience,Interactive game,Free Online game,Brain,Training,English version,French version.Chinese checkers." >

    <meta name = "description"
          content = "Train your brain. Play peg solitaire online. Patience game online. Brainvita game online. English version and French version of the peg solitaire board puzzle.Chinese checkers." >

    <script language = "javascript"
            src = "http://www.ucount.info/hits/HitsParams.js"
            type = "TEXT/JAVASCRIPT" >
    </script >

    <style type = "text/css" >
      .dummy
      {
        border: 1px solid black;
        position: absolute;
        visibility: visible;
        font-size: 4px;
        background-color: blue
      }

      .peg
      {
        background-image: url("p.png");
        background-position: center center;
        background-repeat: no-repeat;
        width: 36;
        height: 36;}

      .ClassGameStatus
      {
	color:  # 8800ff;
	font: bold "Trebuchet MS", sans-serif;
	font-size: 13px;}

    </style >

    <script language = "javascript"
            type = "TEXT/JAVASCRIPT" >
    <!--

       var numPegs;
       var currNumPegs;
       var tableSize;
       var selectStatus;
       var fromID;
       var endPointX;
       var endPointY;

       //var img0 = new Image();
       //img0.src = "images/l.png";

       //var img1 = new Image();
       //img1.src = "images/p.png";

       //var img2 = new Image();
       //img2.src = "images/d.png";

       function Init()
       {
         var i, j, id;

  	 numPegs = document.getElementById('NumOfPegs').value;
         // alert('num Pegs = ' + numPegs);

  	 tableSize = document.getElementById('TableSize').value;
         // alert('table size = ' + tableSize);

  	 cellSize = document.getElementById('CellSize').value;

  	 endPointX = document.getElementById('EndPointX').value;
  	 endPointY = document.getElementById('EndPointY').value;

         currNumPegs = 0;
         selectStatus = 0;
         fromID = '';

         for (i=0; i < tableSize; i++)
         {
           for (j=0; j < tableSize; j++)
           {
             id = 'v'+i+'p'+j;

    	     if (document.getElementById(id).value == 2)
             {
               currNumPegs++; }
           }
         }
       }

       function intVal(val)
       {
         if (val == '0') return 0;
         else if (val == '1') return 1;
         else if (val == '2') return 2;
         else if (val == '3') return 3;
         else if (val == '4') return 4;
         else if (val == '5') return 5;
         else if (val == '6') return 6;
         else if (val == '7') return 7;
         else if (val == '8') return 8;
         else if (val == '9') return 9; }

       function checkEndOfGame()
       {
         var i, j, id, cell;

         // alert('currNumPegs='+currNumPegs);
         for (i=0; i < tableSize; i++)
         {
           var legalMoves = 0;
           for (j=0; j < tableSize; j++)
           {
             id = i+'p'+j;

    	     if (document.getElementById('v'+id).value == 2)
             {
               legalMoves = checkLegalMove(i, j);
               if (legalMoves == 1)
               {
                 break; }
             }
           }
           if (legalMoves == 1)
           {
             break; }
         }

         if (legalMoves == 0)
         {
           if (currNumPegs > 1)
           {
             gameStat = document.getElementById("StatusId");
             gameStat.style.color = '#aa0033';
             gameStat.value = "     No more legal moves. " +
                 currNumPegs+" pegs left on the board."
           }
           else
           {
  	     idv = 'v'+endPointX+'p'+endPointY;
    	     if (document.getElementById(idv).value != 2)
             {
               gameStat = document.getElementById("StatusId");
               gameStat.style.color = '#aa00aa';
               gameStat.value = "  The last peg should be in the center. Try again!!"
             }
    	     else
             {
               gameStat = document.getElementById("StatusId");
               gameStat.style.color = '#00aa00';
               gameStat.value = "      Congratulations!! you have solved the puzzle!"

               cell = document.getElementById("i0p2");
               cell.style.backgroundImage = "url(B.jpg)";
               cell = document.getElementById("i1p2");
               cell.style.backgroundImage = "url(R.jpg)";
               cell = document.getElementById("i2p2");
               cell.style.backgroundImage = "url(A.jpg)";
               cell = document.getElementById("i3p2");
               cell.style.backgroundImage = "url(V.jpg)";
               cell = document.getElementById("i4p2");
               cell.style.backgroundImage = "url(O.jpg)";
               cell = document.getElementById("i5p2");
               cell.style.backgroundImage = "url(es.jpg)";
               cell = document.getElementById("i6p2");
               cell.style.backgroundImage = "url(es.jpg)"; }
           }
         }
         else
         {
           gameStat = document.getElementById("StatusId");
           gameStat.style.color = '#3300aa';
           gameStat.value = "                There are "+currNumPegs+" pegs on the board."
         }
       }

       function checkLegalMove(i, j)
       {
         var i, j, id2, id3, x1, y1, x2, y2, x3, y3;

         x1 = i;
         y1 = j;

         if (x1 > 1)
         {
           x2 = x1-1;
           x3 = x1-2;
           id2 = x2+'p'+y1;
           id3 = x3+'p'+y1;
           if (document.getElementById('v'+id2).value == 2)
           {
             if (document.getElementById('v'+id3).value == 1)
             {
               return 1; }
           }
         }

         if (x1 < (tableSize - 2))
         {
           x2 = x1+1;
           x3 = x1+2;
           id2 = x2+'p'+y1;
           id3 = x3+'p'+y1;
           if (document.getElementById('v'+id2).value == 2)
           {
             if (document.getElementById('v'+id3).value == 1)
             {
               return 1; }
           }
         }

         if (y1 > 1)
         {
           y2 = y1-1;
           y3 = y1-2;
           id2 = x1+'p'+y2;
           id3 = x1+'p'+y3;
           if (document.getElementById('v'+id2).value == 2)
           {
             if (document.getElementById('v'+id3).value == 1)
             {
               return 1; }
           }
         }

         if (y1 < (tableSize - 2))
         {
           y2 = y1+1;
           y3 = y1+2;
           id2 = x1+'p'+y2;
           id3 = x1+'p'+y3;
           if (document.getElementById('v'+id2).value == 2)
           {
             if (document.getElementById('v'+id3).value == 1)
             {
               return 1; }
           }
         }

         return 0; }

       function handleClick(id)
       {
         var id1;
         try
         {
           if (selectStatus == 0)
           {
             id1 = "v"+id;
 	     if (document.getElementById(id1).value == 2)
             {
               fromId = id;
               id1 = 'i'+id;
       	       fromCell = document.getElementById(id1);
               fromCell.style.backgroundImage = "url(l.png)";
               selectStatus = 1;}
           }
           else if (selectStatus == 1)
           {
 	     if (document.getElementById('v'+id).value == 2)
             {
               id1 = 'i'+fromId;
       	       fromCell = document.getElementById(id1);
               fromCell.style.backgroundImage = "url(p.png)";
               fromId = id;
               id1 = 'i'+fromId;
       	       fromCell = document.getElementById(id1);
               fromCell.style.backgroundImage = "url(l.png)";
               return; }


             if (Math.abs(id.charAt(0)-fromId.charAt(0)) == 0)
             {
               if (Math.abs(id.charAt(2)-fromId.charAt(2)) != 2)
               {
                 return; }
               else
               {
                 xb = intVal(id.charAt(0));
                 yb = Math.abs((intVal(id.charAt(2))+intVal(fromId.charAt(2)))/2); }
             }

             else if (Math.abs(id.charAt(0)-fromId.charAt(0)) == 2)
             {
               if (Math.abs(id.charAt(2)-fromId.charAt(2)) != 0)
               {
                 return; }
               else
               {
                 xb = Math.abs(
                     (intVal(id.charAt(0))+intVal(fromId.charAt(0)))/2);
                 yb = intVal(id.charAt(2)); }
             }

             else
             {
               return; }

             // alert('xb='+xb+' yb='+yb)
 	     idb = 'i'+xb+'p'+yb;
 	     idbv = 'v'+xb+'p'+yb;
 	     if (document.getElementById(idbv).value != 2)
             {
               return; }

 	     if (document.getElementById('v'+id).value == 1)
             {
               toId = id;
               id1 = 'i'+id;
       	       toCell = document.getElementById(id1);
               toCell.style.backgroundImage = "url(p.png)";
               toCell.style.backgroundPosition = "center center";
               toCell.style.backgroundRepeat = "no-repeat";
               id1 = 'i'+fromId;
     	       fromCell = document.getElementById(id1);
               fromCell.style.backgroundImage = "url(d.png)";
     	       document.getElementById(idb).style.backgroundImage = "url(d.png)";
 	       document.getElementById('v'+toId).value = 2;
 	       document.getElementById('v'+fromId).value = 1;
 	       document.getElementById(idbv).value = 1;
               selectStatus = 0;
               currNumPegs--;
               checkEndOfGame(); }
           }
         }
         catch(err)
         {
	   alert("Error in function handleClick : "+err.description); }
       }

      -->
    </script>

  </head>


  <body bgcolor="#eeeecc">


    <table align="center">

      <tr>
        <td colspan="5" align="center">
          <font size="5" color="#0000DD">
            <u>
              Peg Solitaire Online
            </u>
          </font>
        </td>
      </tr>

      <tr><td colspan="5">&nbsp;</td></tr>

      <tr>
        <td align="center" colspan="5" width='720'>
          <font color='000000'>English version of peg solitaire puzzle or the patience game.The objective of the game is to empty the board and leave only one <br>peg in the central square.To make a move: click on a peg and then click on the destination square.</font>        </td>
      </tr>

      
      <tr><td colspan="5">&nbsp;</td></tr>

      <tr>
        <td align="center" colspan="5">

          <INPUT TYPE='hidden' 
                       ID='v0p0' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v0p1' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v0p2' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v0p3' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v0p4' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v0p5' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v0p6' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v1p0' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v1p1' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v1p2' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v1p3' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v1p4' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v1p5' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v1p6' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v2p0' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v2p1' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v2p2' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v2p3' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v2p4' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v2p5' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v2p6' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v3p0' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v3p1' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v3p2' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v3p3' 
                       VALUE='1'><INPUT TYPE='hidden' 
                       ID='v3p4' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v3p5' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v3p6' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v4p0' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v4p1' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v4p2' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v4p3' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v4p4' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v4p5' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v4p6' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v5p0' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v5p1' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v5p2' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v5p3' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v5p4' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v5p5' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v5p6' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v6p0' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v6p1' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v6p2' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v6p3' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v6p4' 
                       VALUE='2'><INPUT TYPE='hidden' 
                       ID='v6p5' 
                       VALUE='0'><INPUT TYPE='hidden' 
                       ID='v6p6' 
                       VALUE='0'><INPUT TYPE='hidden' 
                 ID='NumOfPegs' 
                 VALUE='32'><INPUT TYPE='hidden' 
                 ID='TableSize' 
                 VALUE='7'><INPUT TYPE='hidden' 
                 ID='CellSize' 
                 VALUE='36'><INPUT TYPE='hidden' 
                 ID='EndPointX' 
                 VALUE='3'><INPUT TYPE='hidden' 
                 ID='EndPointY' 
                 VALUE='3'><table><tr><td width='36' 
                    id='i0p0'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i1p0'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i2p0'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("2p0")'></td><td width='36' 
                    id='i3p0'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("3p0")'></td><td width='36' 
                    id='i4p0'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("4p0")'></td><td width='36' 
                    id='i5p0'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i6p0'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td></tr><tr><td width='36' 
                    id='i0p1'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i1p1'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i2p1'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("2p1")'></td><td width='36' 
                    id='i3p1'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("3p1")'></td><td width='36' 
                    id='i4p1'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("4p1")'></td><td width='36' 
                    id='i5p1'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i6p1'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td></tr><tr><td width='36' 
                    id='i0p2'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("0p2")'></td><td width='36' 
                    id='i1p2'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("1p2")'></td><td width='36' 
                    id='i2p2'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("2p2")'></td><td width='36' 
                    id='i3p2'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("3p2")'></td><td width='36' 
                    id='i4p2'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("4p2")'></td><td width='36' 
                    id='i5p2'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("5p2")'></td><td width='36' 
                    id='i6p2'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("6p2")'></td></tr><tr><td width='36' 
                    id='i0p3'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("0p3")'></td><td width='36' 
                    id='i1p3'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("1p3")'></td><td width='36' 
                    id='i2p3'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("2p3")'></td><td width='36' 
                    id='i3p3'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class=''
                    onclick='handleClick("3p3")'></td><td width='36' 
                    id='i4p3'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("4p3")'></td><td width='36' 
                    id='i5p3'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("5p3")'></td><td width='36' 
                    id='i6p3'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("6p3")'></td></tr><tr><td width='36' 
                    id='i0p4'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("0p4")'></td><td width='36' 
                    id='i1p4'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("1p4")'></td><td width='36' 
                    id='i2p4'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("2p4")'></td><td width='36' 
                    id='i3p4'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("3p4")'></td><td width='36' 
                    id='i4p4'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("4p4")'></td><td width='36' 
                    id='i5p4'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("5p4")'></td><td width='36' 
                    id='i6p4'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("6p4")'></td></tr><tr><td width='36' 
                    id='i0p5'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i1p5'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i2p5'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("2p5")'></td><td width='36' 
                    id='i3p5'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("3p5")'></td><td width='36' 
                    id='i4p5'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("4p5")'></td><td width='36' 
                    id='i5p5'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i6p5'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td></tr><tr><td width='36' 
                    id='i0p6'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i1p6'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i2p6'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("2p6")'></td><td width='36' 
                    id='i3p6'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("3p6")'></td><td width='36' 
                    id='i4p6'
                    height='36' 
                    align='center'
                    bgcolor='#99dd99'
                    class='peg'
                    onclick='handleClick("4p6")'></td><td width='36' 
                    id='i5p6'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td><td width='36' 
                    id='i6p6'
                    height='36' 
                    align='center'
                    bgcolor='#eeeecc'
                    class=''
                    ></td></tr></table>
        </td>
      </tr>

      <tr><td colspan="5">&nbsp;</td></tr>

      <TR>
        <TD align="center" colspan="2">
                    <INPUT TYPE="text" 
                 class="ClassGameStatus" 
                 NAME="GameStatus"
                 ID="StatusId"
                 Value="            &nbsp;&nbsp;&nbsp;&nbsp;There are 32 pegs on the board."
                 SIZE="50">    
        </TD>
      </tr>

      <tr><td colspan="5">&nbsp;</td></tr>



      <tr>
        <td colspan="5" align="center">
          <form name="form1" METHOD=POST ACTION="index.php">
          <table>
            <tr>
              <td>
                <select name="GameVersion" 
                        onChange="form1.submit();">
                  <option value="1" selected>English Version</option>
                  <option value="2" >French Version</option>
                </select>
              </td>

              <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>

              <td>
                <INPUT TYPE="submit" 
                       NAME="NewGame"
                       VALUE="New Game">
              </td>
            </tr>
          </table>
          </form>
        </td>


  <!--TD align="center">
               <a href="../index.php">
                 <img src="../images/home.jpg" 
                      alt="home" 
                      height="32" 
                      width="32" />
               </a>
             </TD-->


      </tr>



    

    <tr>
    <td align="center" colspan="5">
    <table>
    <tr>
    <td align="center">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- au_webgamesonline_pegsolitaire_728x90 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-3899981072920923"
     data-ad-slot="7416145199"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
    </td>
    </tr>
    </table>
    </td>
    </tr>



      <tr><td  align="center" colspan="10">&nbsp;</td></tr>

      <tr>
        <td align="center" colspan="5">
          <hr>
            <a href="../index.php"><font size="2">Home</font></a>
        </td>
      </tr>

    </table>

    <img src="p.png" 
         width="0" 
         id="temp"
         height="0" 
         alt="" >

      <script language="javascript" 
              type="TEXT/JAVASCRIPT">
        Init();
      </script>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-27789966-28"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-27789966-28');
</script>

  </body>

</html>
