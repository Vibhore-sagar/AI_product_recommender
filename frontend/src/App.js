import { useState } from "react";
import products from "./data/products";

function App() {
  const [preference, setPreference] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const fetchRecommendations = async () => {
    const response = await fetch("http://localhost:8000/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        preference,
        products
      })
    });

    const data = await response.json();
    setRecommendations(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Product Recommendation System</h2>

      <input
        type="text"
        placeholder="I want a phone under $500"
        value={preference}
        onChange={(e) => setPreference(e.target.value)}
        style={{ width: "300px" }}
      />

      <button onClick={fetchRecommendations}>Recommend</button>

      <h3>Recommended Products</h3>
      <ul>
        {recommendations.map((product) => (
          <li key={product.id}>
            {product.name} - ${product.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
