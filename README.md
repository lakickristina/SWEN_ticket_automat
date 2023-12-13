!! Change this document for your own project by removing the placeholder text, adding your own text, adding helpful sections etc. etc. !!

# Ticketautomat

In diesem Projekt geht es um einen Ticketautomaten, bei dem man eine Auswahl an verschiedenen Tickets hat. 
Zusätzlich werden einem Münzen gegeben, mit denen man das Ticket bezahlen kann. 
Es sollte möglich sein, Tickets zu wählen, diese zu bezahlen, nach Bedarf Rückgeld
zu erhalten sowie, dass das Ticket ausgegeben wird.

## Get started
Auf der linken Seite sind die Tickets auegführt und auf der rechten die Münzmöglichkeiten. Nach der Auswhal
eines Tickets, können die Münzen angewählt werden, sodass das Ticket bezahlt werden kann. Wurde der 
Betrag noch nicht erreicht, wird links der aktuelle Saldo angezeigt. Sobald der Betrag erreicht worden
ist, bekommt man das Ticket und falls nötig das Rückgeld. Bevor der Betrag des Tickets erreicht worden
ist, ist es jederzeit möglich den Vorgang über den Button "Ticket stornieren" abzubrechen und allfällig 
bezahltes Geld wieder zurückzuerhalten. Das Ticket wird unten links und allfälliges Rückgeld wird rechts ausgegeben. 
Um den Ticketautomaten zu beenden, muss man rechts unten auf den Button "Schliessen" klicken. 

Aus Zeitgründen wurde darauf verzichtet, die Möglichkeit zu geben, mehrere Tickets aufs Mal zu wählen. 

## Understanding the sources

Der Ticketautomat basiert auf verschiedenen Layouts, welche entweder horizontal oder vertikal aufgebaut sind. 
Somit konnten die Buttons einerseits untereinander, andererseits aber auch nebeneinander abgebildet werden. 
Für die graphischen Elemente wurde die Library von PyQt5 verwendet.