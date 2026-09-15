A collection of useful scripts i Use

1. playlists: It uses csv files to import songs and export them to the ytmusicapi.

(step by step process)

> install yytmusicapi on your system. 

> run ytmusicapi setup

> open ytmusic on your browser and run inspect.

> go to network tab and on your main page switch to library and home one by one.

> now on your networks tab, use filter "browse" to search for the apiinfo fetch.

> right click on that and go to copy url> copy header request.

> on your terminal, run  ytmusicapi browse and paste that link there.

> Hit enter and press Ctrl+D

> Find the browse.json file on your system.

> Open the script in some editor & replace the name of the browse file with your own and use "r" flag to prvide its location.

> jump to the last of the script and rename the path of the csv file to your own and name the playlist the name you want to have for it in the name field. 

> save the script, exit & run it. 

> see the magic happen.
