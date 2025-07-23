// ovenTime returns the amount in minutes that the lasagna should stay in the
// oven (40).
int ovenTime() {
    return 40;
}

/* remainingOvenTime returns the remaining
   minutes based on the actual minutes already in the oven.
*/
int remainingOvenTime(int actualMinutesInOven) {
    return ovenTime() - actualMinutesInOven;
}

/* preparationTime returns an estimate of the preparation time based on the
   number of layers and the necessary time per layer (2 min).
*/
int preparationTime(int numberOfLayers) {
    return numberOfLayers * 2;;
}

// elapsedTime calculates the total time spent to create and bake the lasagna so
// far.
int elapsedTime(int numberOfLayers, int actualMinutesInOven) {
    return preparationTime(numberOfLayers) + remainingOvenTime(actualMinutesInOven);
}
