{% include navbar.html %}

# Description
Our create task is a game that will allow the user 5 attempts to guess a country and throughout those 5 attempts will give them 4 hints. After the 5 attempts, the game ends if they didn't guess correctly, however, if there is a correct guess then the game will tell the user that they have won. 
### Features:
* input bar for the guessing of the countries
* A Guess button to send the guess through the system and output correct or incorrect
* A Clear button to clear the input bar of your current guess
* A New button to start a new game with a new country
* 4 hints: 1. The first letter, 2. The last letter, 3. The number of letters, 4. The continent the country is on
* If correct, there will be a popup indicating that the user was correct and telling the user how many attempts it took. If not correct after 5 tries, the popup will tell the user what the answer was. 

The user can test their ability at guessing countries or learn the names of new countries that they'd previously never heard of. 
# Possible Other Ideas
We could add facts about the different countries if you guess the correct and if you guess them wrong at the end of each game so you could be learning something new about the different countries that you are guessing. We could also show an outline of the country, so the user can guess based on that.

# Videos
Isaac: https://user-images.githubusercontent.com/60956151/155924084-55305659-67d8-4cb0-99a1-2860af7af137.mp4

# Final Code
[Code](https://replit.com/@IsaacLe2/Countryguesser#index.html)
# Questions

### Isaac
3a. 
i. The program is a game where the user inputs guesses to try and determine a randomly generated country. The user can use this to test their ability at guessing countries or find out about countries they never even knew about before.

ii. In the video, different guesses were inputted and for each guess, a new hint was given. When the answer was guessed correctly, the popup told the user that they were correct and told the user how many guesses it took. When the user was incorrect after 5 tries, a popup told the user that they were incorrect and told them the correct answer.

iii. The input of the program by the user is the country they guess. The output is a new hint for each time the user guesses and is incorrect. If the user is correct, the output is a popup that tells the user that they were correct and how many attempts it took. If the user is wrong for 5 tries, the output is a popup telling the user what the actual answer was.

3b.
i. `var country = new Array(177);`

    `country[0] = "AFGHANISTAN";`
    `country[1] = "ALBANIA";`
    `country[2] = "ALGERIA";`
    `country[3] = "AMERICA";`
    `country[4] = "ANDORRA";`
    `country[5] = "ANGOLA";`
    `country[6] = "ARGENTINA";`
    `country[7] = "ARMENIA";`
    `country[8] = "AUStrALIA";`
    `country[9] = "AUStrIA";`
    `country[10] = "AZERBAIJAN";`
    `country[11] = "BAHAMAS";`
    `country[12] = "BAHRAIN";`
    `country[13] = "BANGLADESH";`
    `country[14] = "BARBADOS";`
    `country[15] = "BELARUS";`
    `country[16] = "BELGIUM";`
    `country[17] = "BELIZE";`
    `country[18] = "BENIN";`
    `country[19] = "BHUTAN";`
    `country[20] = "BOLIVIA";`
    `country[21] = "BOSNIA HERZEGOVINA";`
    `country[22] = "BOTSWANA";`
    `country[23] = "BRAZIL";`
    `country[24] = "BRUNEI";`
    `country[25] = "BULGARIA";`
    `country[26] = "BURKINA";`
    `country[27] = "BURUNDI";`
    `country[28] = "CAMBODIA";`
    `country[29] = "CAMEROON";`
    `country[30] = "CANADA";`
    `country[31] = "CAPE VERDE ISLANDS";`
    `country[32] = "CHAD";`
    `country[33] = "CHILE";`
    `country[34] = "CHINA";`
    `country[35] = "COLOMBIA";`
    `country[36] = "COMOROS";`
    `country[37] = "CONGO";`
    `country[38] = "COSTA RICA";`
    `country[39] = "CROATIA";`
    `country[40] = "CUBA";`
    `country[41] = "CYPRUS";`
    `country[42] = "CZECH REPUBLIC";`
    `country[43] = "DENMARK";`
    `country[44] = "DJIBOUTI";`
    `country[45] = "DOMINICAN REPUBLIC";`
    `country[46] = "ECUADOR";`
    `country[47] = "EGYPT";`
    `country[48] = "EL SALVADOR";`
    `country[49] = "ERItrEA";`
    `country[50] = "ESTONIA";`
    `country[51] = "ETHIOPIA";`
    `country[52] = "FIJI";`
    `country[53] = "FINLAND";`
    `country[54] = "FRANCE";`
    `country[55] = "GABON";`
    `country[56] = "GAMBIA";`
    `country[57] = "GEORGIA";`
    `country[58] = "GERMANY";`
    `country[59] = "GHANA";`
    `country[60] = "GREECE";`
    `country[61] ="GRENADA";`
    `country[62] = "GUATEMALA";`
    `country[63] = "GUINEA";`
    `country[64] = "HAITI";`
    `country[65] = "HOLLAND";`
    `country[66] = "HONDURAS";`
    `country[67] = "HONG KONG";`
    `country[68] = "HUNGARY";`
    `country[69] = "ICELAND";`
    `country[70] = "INDIA";`
    `country[71] = "INDONESIA";`
    `country[72] = "IRAN";`
    `country[73] = "IRAQ";`
    `country[74] = "ISRAEL";`
    `country[75] = "ITALY";`
    `country[76] = "JAMAICA";`
    `country[77] = "JAPAN";`
    `country[78] = "JORDAN";`
    `country[79] = "KAZAKHSTAN";`
    `country[80] = "KENYA";`
    `country[81] = "KYRGYZSTAN";`
    `country[82] = "KIRIBATI";`
    `country[83] = "KOREA";`
    `country[84] = "KUWAIT";`
    `country[85] = "LAOS";`
    `country[86] = "LATVIA";`
    `country[87] = "LEBANON";`
    `country[88] = "LESOTHO";`
    `country[89] = "LIBERIA";`
    `country[90] = "LIBYA";`
    `country[91] = "LIECHTENSTEIN";`
    `country[92] = "LITHUANIA";`
    `country[93] = "LUXEMBOURG";`
    `country[94] = "MADAGASCAR";`
    `country[95] = "MALAWI";`
    `country[96] = "MALAYSIA";`
    `country[97] = "MALDIVES";`
    `country[98] = "MALI";`
    `country[99] = "MALTA";`
    `country[100] = "MAURITANIA";`
    `country[101] = "MAURITIUS";`
    `country[102] = "MEXICO";`
    `country[103] = "MOLDOVA";`
    `country[104] = "MONACO";`
    `country[105] = "MONGOLIA";`
    `country[106] = "MONTENEGRO";`
    `country[107] = "MOROCCO";`
    `country[108] = "MOZAMBIQUE";`
    `country[109] = "MYANMAR";`
    `country[110] = "NAMIBIA";`
    `country[111] = "NAURU";`
    `country[112] = "NEPAL";`
    `country[113] = "NETHERLANDS";`
    `country[114] = "NEW ZEALAND";`
    `country[115] = "NICARAGUA";`
    `country[116] = "NIGERIA";`
    `country[117] = "NORWAY";`
    `country[118] = "OMAN";`
    `country[119] = "PAKISTAN";`
    `country[120] = "PANAMA";`
    `country[121] = "PAPUA NEW GUINEA";`
    `country[122] = "PARAGUAY";`
    `country[123] = "PERU";`
    `country[124] = "PHILIPPINES";`
    `country[125] = "POLAND";`
    `country[126] = "PORTUGAL";`
    `country[127] = "QATAR";`
    `country[128] = "ROMANIA";`
    `country[129] = "RUSSIA";`
    `country[130] = "RWANDA";`
    `country[131] = "SAN MARINO";`
    `country[132] = "SAUDI ARABIA";`
    `country[133] = "SENEGAL";`
    `country[134] = "SEYCHELLES";`
    `country[135] = "SIERRA LEONE";`
    `country[136] = "SINGAPORE";`
    `country[137] = "SLOVAKIA";`
    `country[138] = "SLOVENIA";`
    `country[139] = "SOLOMON ISLANDS";`
    `country[140] = "SOMALIA";`
    `country[141] = "SOUTH AFRICA";`
    `country[142] = "SPAIN";`
    `country[143] = "SRI LANKA";`
    `country[144] = "SUDAN";`
    `country[145] = "SURINAME";`
    `country[146] = "SWAZILAND";`
    `country[147] = "SWEDEN";`
    `country[148] = "SWITZERLAND";`
    `country[149] = "SYRIA";`
    `country[150] = "TAIWAN";`
    `country[151] = "TAJIKISTAN";`
    `country[152] = "TANZANIA";`
    `country[153] = "THAILAND";`
    `country[154] = "TOGO";`
    `country[155] = "TONGA";`
    `country[156] = "TRINIDAD AND TOBAGO";`
    `country[157] = "TUNISIA";`
    `country[158] = "TURKEY";`
    `country[159] = "TURKMENISTAN";`
    `country[160] = "TUVALU";`
    `country[161] = "UGANDA";`
    `country[162] = "UKRAINE";`
    `country[163] = "UNITED ARAB EMIRATES";`
    `country[164] = "URUGUAY";`
    `country[165] = "UZBEKISTAN";`
    `country[166] = "VANUATU";`
    `country[167] = "VATICAN CITY";`
    `country[168] = "VENEZUELA";`
    `country[169] = "VIETNAM";`
    `country[170] = "WEST INDIES";`
    `country[171] = "WESTERN SAMOA";`
    `country[172] = "YEMEN";`
    `country[173] = "YUGOSLAVIA";`
    `country[174] = "ZAIRE";`
    `country[175] = "ZAMBIA";`
    `country[176] = "ZIMBABWE";`
ii.  `function guessit()`
    `{`
        `var guess = document.form1.guess1.value;`
        `tries++;`
        `window.status = "tries : " + tries + " ";`
        `switch(tries)`
        `{`
            `case 1:`
                `document.form1.hint.value = "First Hint : The country name starts with " + temp.charAt(0);`
                `break;`

            `case 2:`
                `document.form1.hint.value = "Second Hint : The country name ends with " + temp.charAt(temp.length - 1);`
                `break;`

            `case 3:`
                `document.form1.hint.value = "Third Hint : The country name has " + temp.length + " characters";`
                `break;`

            `case 4:`
                `document.form1.hint.value = "Last Hint : The country is in " + temp2;`
                `break;`

            `default:`
                `document.form1.hint.value = "No hints are available";`
        `}`
        `if(guess.toUpperCase() == temp)`
        `{`
            `if(window.confirm("Absolutely Right! Yes the country was " + temp + ". This took " + tries + " tries.\nDo you want to play again?"))`
                `window.location.reload();`
        `}`
        `else`
        `{`
            `if(tries == 5)`
            `{`
                `if(window.confirm("Sorry ! You've used up your 5 tries. The country was  " + temp + "\nDo you want to play again?"))`
                `{`
                    `window.location.reload();`
                    `document.form1.hint.value = "Enter your guess below and click on Guess!";`
                `}`
            `}`
        `}`
    `}`

iii) The name of the list is country

iv) The data in the list is the different names of countries around the world, which are represented by country[number].

v) Without this list the program wouldn't run because we wouldn't have the names of the countries that we are trying to guess so there wouldn't be any countries in the game. Also, by doing a list of country[number] to represent each country, we are able to easily randomize it and select a country as what the user has to guess.

3c.
i)    ` var sr = Math.floor(Math.random() * 177);`
    `var temp = country[sr];`
    `var temp2 = continent[sr];`
    `var tries = 0;`

    `function guessit()`
    `{`
        `var guess = document.form1.guess1.value;`
        `tries++;`
        `window.status = "tries : " + tries + " ";`
        `switch(tries)`
        `{`
            `case 1:`
                `document.form1.hint.value = "First Hint : The country name starts with " + temp.charAt(0);`
                `break;`

            `case 2:`
                `document.form1.hint.value = "Second Hint : The country name ends with " + temp.charAt(temp.length - 1);`
                `break;`

            `case 3:`
                `document.form1.hint.value = "Third Hint : The country name has " + temp.length + " characters";`
                `break;`

            `case 4:`
                `document.form1.hint.value = "Last Hint : The country is in " + temp2;`
                `break;`

            `default:`
                `document.form1.hint.value = "No hints are available";`
        `}`
        `if(guess.toUpperCase() == temp)`
        `{`
            `if(window.confirm("Absolutely Right! Yes the country was " + temp + ". This took " + tries + " tries.\nDo you want to play again?"))`
                `window.location.reload();`
        `}`
        `else`
        `{`
            `if(tries == 5)`
            `{`
                `if(window.confirm("Sorry ! You've used up your 5 tries. The country was  " + temp + "\nDo you want to play again?"))`
                `{`
                    `window.location.reload();`
                    `document.form1.hint.value = "Enter your guess below and click on Guess!";`
                `}`
            `}`
        `}`
    `}`

ii)             ` <input type=button  class=td2 value=Guess! onClick=guessit()`
                   `title="Click here to get a hint or check your guess.">`

iii) This procedure obtains and stores the correct country as the answer and gives the user 5 attempts to guess with a hint after each wrong attempt. It also tells the user if they have won or if they have lost at the end.

iv)  The procedure take a random country out of the list of countries and stores it as the correct answer. You are then given 5 attempts to guess a country and after each attempt you give the player a hint. If the user guesses the correct answer in the set amount of tries, then a message will pop up saying that the user has won and ask if they want to play again. If the user can't get the correct answer in the set amount of tries, then a message will pop up saying that the user has lost, giving them the correct country, and asking if they want to play again.

3d.

i) 
First Call: Calls to the procedure guessit so that the user can get whether or not they got their guess correct or wrong and displaying the correct messages or giving the correct hints.

Second Call: Calls to the procedure new game so that the user can start a new game if they want obtaining a new country as the right country and starting the game all over again.

ii)
First Call: If the guess is correct, wrong, and how many attempts there have been so far in the game

Second Call: Determine if the user clicked yes or no to restart the game

iii)
First Call: If the guess is correct, a win message will display to the user and ask if they want a new game. If the guess is wrong and the number of attempts is less than 5 then a hint will appear. If the guess is wrong and the number of attempts is 5 and over then the game will tell the user the country and will ask if they want to play a new game.

Second Call: If the user clicked yes the guessit function will run again giving the user a new country that they can guess for. If they user clicked no then the guessit function will not run again and the user will stay on the same country and page that they are currently on.
