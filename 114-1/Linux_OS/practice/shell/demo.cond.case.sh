#!/bin/bash
# demonstrate conditional expressions - case

PS3="Choose a flower which you like:"
select flower in Sunflower Tulip Orchid Carnation Lily Peony NoneOfAbove
do
	case $flower in
		Sunflower) echo "Flower meanings: Sunflower signifies pure thoughts.";;
		Tulip) echo "Flower meanings: Tulip signifies a declaration of love.";;
		Orchid) echo "Flower meanings: Orchid symbolizes refinement, thoughtfulness and mature charm.";;
		Carnation) echo "Flower meanings: Carnation symbolizes pride and beauty.";;
		Lily) echo "Flower meanings: Lily symbolizes purity and refined beauty.";;
		Peony) echo "Flower meanings: Peony symbolizes bashfulness and compassion.";;
		NoneOfAbove) echo "Ooh... So sad. :(";;
		*) echo "You press the wrong key!"
			exit;;
	esac
	
done

exit 0
