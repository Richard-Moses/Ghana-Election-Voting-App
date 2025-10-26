template = """
<!DOCTYPE html>
<html>
<head>
  <title>Ghana Election Voting App</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: #f4f4f4;
      padding-top: 50px;
    }
    h2 {
      color: #333;
    }
    .vote-button {
      font-size: 1.5em;
      padding: 15px 30px;
      margin: 20px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      color: white;
    }
    .npp {
      background: linear-gradient(to right, red, white, blue);
    }
    .ndc {
      background: linear-gradient(to right, red, black, green);
    }
    .results {
      margin-top: 30px;
      font-size: 1.2em;
    }
  </style>
</head>
<body>
  <h2>🇬🇭 Ghana Election Voting App</h2>
  <form method="POST">
    <button class="vote-button npp" name="vote" value="NPP">Vote NPP</button>
    <button class="vote-button ndc" name="vote" value="NDC">Vote NDC</button>
  </form>
  <div class="results">
    <p><strong>NPP Votes:</strong> {{npp}}</p>
    <p><strong>NDC Votes:</strong> {{ndc}}</p>
  </div>
</body>
</html>
"""