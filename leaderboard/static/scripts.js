window.addEventListener('DOMContentLoaded', () => {
    const leaderboardTable = document.getElementById('leaderboard-table');

    // Function to fetch leaderboard data
    const fetchLeaderboardData = async () => {
        try {
            const response = await fetch('api/leaderboard/');
            // console.log("reached here")
            const data = await response.json();
            // console.log(data)
            // return data.leaderboard;
            return data;
        } catch (error) {
            console.error('Error fetching leaderboard data:', error);
        }
    };

    // Function to populate the leaderboard table
    const populateLeaderboardTable = async () => {
        const leaderboardData = await fetchLeaderboardData();
        // console.log(leaderboardData)
        if (leaderboardData) {
            console.log("passed if check")
            leaderboardData.forEach(user => {
                const row = leaderboardTable.insertRow();
                row.innerHTML = `
                    <td>${user.name}</td>
                    <td>${user.score}</td>
                `;
                // console.log(row.innerHTML)
            });
        }
    };

    populateLeaderboardTable();
});
