// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract NiftyITPrediction {
    // State variables to store model predictions, combined prediction, and actual event
    int8 public model1Prediction;
    int8 public model2Prediction;
    int8 public model3Prediction;
    int8 public combinedPrediction;
    int8 public actualEvent;

    // Weights for each model
    uint256 public weight1 = 1;
    uint256 public weight2 = 1;
    uint256 public weight3 = 1;

    // Event to be emitted when weights are updated
    event WeightsUpdated(
        uint256 newWeight1,
        uint256 newWeight2,
        uint256 newWeight3
    );

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to certain functions to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to set predictions from the models, combined prediction, and actual event
    function setPredictions(
        int8 _model1Prediction,
        int8 _model2Prediction,
        int8 _model3Prediction,
        int8 _combinedPrediction,
        int8 _actualEvent
    ) public onlyOwner {
        model1Prediction = _model1Prediction;
        model2Prediction = _model2Prediction;
        model3Prediction = _model3Prediction;
        combinedPrediction = _combinedPrediction;
        actualEvent = _actualEvent;

        // After setting predictions, check if there is a mismatch
        checkMismatch();
    }

    // Internal function to check if the combined prediction matches the actual event
    function checkMismatch() internal {
        if (combinedPrediction != actualEvent) {
            // Increase the weight of the model(s) that correctly predicted the actual event
            if (model1Prediction == actualEvent) {
                weight1++;
            }
            if (model2Prediction == actualEvent) {
                weight2++;
            }
            if (model3Prediction == actualEvent) {
                weight3++;
            }

            // Emit an event when weights are updated
            emit WeightsUpdated(weight1, weight2, weight3);
        }
    }

    // Function to retrieve the current weights of the models
    function getWeights() public view returns (uint256, uint256, uint256) {
        return (weight1, weight2, weight3);
    }
}
