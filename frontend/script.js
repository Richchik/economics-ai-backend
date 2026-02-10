function analyze() {
    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            revenue: document.getElementById("revenue").value,
            expenses: document.getElementById("expenses").value,
            electricity: document.getElementById("electricity").value,
            waste: document.getElementById("waste").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = `
            <h3>Status: ${data.status}</h3>
            <p>Profit: ₹${data.profit}</p>
            <p>Business Score: ${data.business_score}</p>
            <p>Sustainability Score: ${data.sustainability_score}</p>
            <p>Final Score: ${data.final_score}</p>
        `;
    });
}
