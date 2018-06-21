import json

json_str = '''[
  [
    {
      "content": "${agreement_no}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 352,
      "endPos": 367
    }
  ],
  [
    {
      "content": "${attorn_cardType}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 443,
      "endPos": 461
    }
  ],
  [
    {
      "content": "${attorn_idNum}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 485,
      "endPos": 500
    }
  ],
  [
    {
      "content": "${assignee_cardType}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 595,
      "endPos": 615
    }
  ],
  [
    {
      "content": "${assignee_idNum}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 639,
      "endPos": 656
    }
  ],
  [
    {
      "content": "${borrowerUserName}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 1662,
      "endPos": 1681
    }
  ],
  [
    {
      "content": "${cardType}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 1686,
      "endPos": 1697
    }
  ],
  [
    {
      "content": "${borrowerIdnum}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 1702,
      "endPos": 1718
    }
  ],
  [
    {
      "content": "${fileNo}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 1845,
      "endPos": 1854
    }
  ],
  [
    {
      "content": "${expect}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 1992,
      "endPos": 2001
    }
  ],
  [
    {
      "content": "${expect}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2007,
      "endPos": 2016
    }
  ],
  [
    {
      "content": "${boAmountUpper}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2048,
      "endPos": 2064
    }
  ],
  [
    {
      "content": "${boAmountLower}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2072,
      "endPos": 2088
    }
  ],
  [
    {
      "content": "${boRate}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2206,
      "endPos": 2215
    }
  ],
  [
    {
      "content": "${boTitle}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2332,
      "endPos": 2342
    }
  ],
  [
    {
      "content": "${boBeginTime}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2459,
      "endPos": 2473
    }
  ],
  [
    {
      "content": "${boEndTime}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2475,
      "endPos": 2487
    }
  ],
  [
    {
      "content": "${transPrice}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2608,
      "endPos": 2621
    }
  ],
  [
    {
      "content": "${repaymentData}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 2694,
      "endPos": 2710
    }
  ],
  [
    {
      "content": "${handingFeeRate}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 5328,
      "endPos": 5345
    }
  ],
  [
    {
      "content": "${arbitrate_name}",
      "isParticipating": true,
      "groupNum": 0,
      "groupName": null,
      "startPos": 6419,
      "endPos": 6436
    }
  ]
]'''
# decode json str to object
list_json = json.loads(json_str)
list_contents = []
[list_contents.append((each[0]['content'])[2:(each[0]['content']).rfind('}')]) for each in list_json]
[print("public static final String " + each.upper() + '="' + each + '";') for each in list_contents]
# [print((each[0]['content']).rfind('}')) for each in list_json]
