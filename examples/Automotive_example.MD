## Automobile Insurance:
1. If the vehicle type is a sedan and the claim value is less than $50,000, the deductible percentage is 15%. Otherwise its 20%.
2. If the vehicle type is a sports car and the claim value is less than 80,000. deductible percentage is 20$ Otherwise its 25%

## Oupuut from the model
```json
{
  "rules": [
    {
      "conditions": [
        {
          "field": "vehicle_type",
          "operator": "==",
          "value": "sedan",
          "sub_conditions": []
        },
        {
          "field": "claim_value",
          "operator": "<",
          "value": 50000,
          "sub_conditions": []
        }
      ],
      "condition_operator": "and",
      "outcome": {
        "field": "deductible_percentage",
        "operator": "=",
        "value": 15
      }
    },
    {
      "conditions": [
        {
          "field": "vehicle_type",
          "operator": "==",
          "value": "sedan",
          "sub_conditions": []
        },
        {
          "field": "claim_value",
          "operator": ">=",
          "value": 50000,
          "sub_conditions": []
        }
      ],
      "condition_operator": "and",
      "outcome": {
        "field": "deductible_percentage",
        "operator": "=",
        "value": 20
      }
    },
    {
      "conditions": [
        {
          "field": "vehicle_type",
          "operator": "==",
          "value": "sports car",
          "sub_conditions": []
        },
        {
          "field": "claim_value",
          "operator": "<",
          "value": 80000,
          "sub_conditions": []
        }
      ],
      "condition_operator": "and",
      "outcome": {
        "field": "deductible_percentage",
        "operator": "=",
        "value": 20
      }
    },
    {
      "conditions": [
        {
          "field": "vehicle_type",
          "operator": "==",
          "value": "sports car",
          "sub_conditions": []
        },
        {
          "field": "claim_value",
          "operator": ">=",
          "value": 80000,
          "sub_conditions": []
        }
      ],
      "condition_operator": "and",
      "outcome": {
        "field": "deductible_percentage",
        "operator": "=",
        "value": 25
      }
    }
  ]
}
