async function getRecommendations() {
    const queryInput = document.getElementById("query");
    const query = queryInput.value.trim();
    const topN = document.getElementById("topN").value;
    const status = document.getElementById("status");
    const results = document.getElementById("results");
    const resultsHeader = document.getElementById("resultsHeader");
    const resultsCount = document.getElementById("resultsCount");

    if (!query) {
        status.style.color = "#f43f5e";
        status.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter a product query or catalogue ID.';
        return;
    }

    // Reset Display
    status.style.color = "#06b6d4";
    status.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Searching vector space for similar products...';
    results.innerHTML = "";
    resultsHeader.style.display = "none";

    try {
        const response = await fetch("/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                query: query,
                top_n: Number(topN)
            })
        });

        const data = await response.json();

        if (!response.ok) {
            status.style.color = "#f43f5e";
            status.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> ${data.error || "Something went wrong."}`;
            return;
        }

        if (!data.recommendations || data.recommendations.length === 0) {
            status.style.color = "#fbbf24";
            status.innerHTML = '<i class="fa-solid fa-circle-info"></i> No matching recommendations found.';
            return;
        }

        status.style.color = "#10b981";
        status.innerHTML = `<i class="fa-solid fa-circle-check"></i> Found top ${data.recommendations.length} relevant products!`;

        // Display Header Count
        resultsHeader.style.display = "flex";
        resultsCount.textContent = `${data.recommendations.length} Results`;

        // Render Recommendations
        data.recommendations.forEach((product, index) => {
            const card = document.createElement("div");
            card.className = "product-card";

            const simScore = (product.similarity_score * 100).toFixed(1);

            card.innerHTML = `
                <div>
                    <div class="card-header">
                        <span class="rank-tag">#${index + 1}</span>
                        <span class="similarity-badge"><i class="fa-solid fa-bolt"></i> ${simScore}% Match</span>
                    </div>
                    <h3>${product.name}</h3>
                </div>
                <div class="card-meta">
                    <div class="meta-item">
                        <span>Product ID:</span>
                        <strong>${product.product_id}</strong>
                    </div>
                    <div class="meta-item">
                        <span>Main Category:</span>
                        <strong>${product.main_category || 'N/A'}</strong>
                    </div>
                    <div class="meta-item">
                        <span>Subcategory:</span>
                        <strong>${product.sub_category || 'N/A'}</strong>
                    </div>
                </div>
            `;

            results.appendChild(card);
        });

    } catch (error) {
        status.style.color = "#f43f5e";
        status.innerHTML = '<i class="fa-solid fa-wifi"></i> Unable to connect to backend server.';
    }
}