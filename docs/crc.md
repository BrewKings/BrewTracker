## Batch:
	R: Store details of a specific Batch
	C: BatchDatabase

## BatchDatabase:
	R: Store all created batches
	C:

## TastingNotes:
	R: Store Batch tasting notes
	C: Batch

## BrewingNotes:
	R: Store Batch brewing notes
	C: Batch, Ingredients, Step

## Ingredients:
	R: Store ingredients of a batch
	C: Ingredient

## Ingredient: 
	R: Stores name, type, quantity, and time of addition of an ingredient
	C: TimeStamp

## TimeStamp:
	R: DateTime object to be attached to another object to date it. 
	R: Stores date and time of creation
	C: 

## Step:
	R: Store information of one step in batch creation
	C: BrewingNotes
