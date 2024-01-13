function growBranch(parent, level, angle, delay) {
    // Create a new branch element
    var branch = document.createElement('div');
    branch.className = 'branch';
    branch.style.height = `${50 / level}%`; // Decrease height as we go down the levels
    branch.style.transform = `rotate(${angle}deg)`;
    branch.style.opacity = '1'; // Make branch visible
    branch.style.animation = `growBranch 2s ${delay}s forwards`; // Animation with delay
    parent.appendChild(branch); // Add the new branch to its parent

    // If we haven't reached the last level, create two more branches
    if (level < 3) {
        growBranch(branch, level + 1, 20, delay + 2); // Create right branch at next level
        growBranch(branch, level + 1, -20, delay + 2); // Create left branch at next level
    }
}

// Start growing branches from the trunk
growBranch(document.getElementById('tree'), 1, 0, 0);
