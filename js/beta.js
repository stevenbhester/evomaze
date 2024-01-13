function createBranch(level, angle, delay) {
    var branch = document.createElement('div');
    branch.className = 'branch';
    branch.style.height = `${33 * level}%`; // Height relative to the level
    branch.style.transform = `translateX(-50%) rotate(${angle}deg)`;
    branch.style.animation = `growBranch 2s ${delay}s forwards`;
    return branch;
}

function growBranches() {
    var tree = document.getElementById('tree');
    var level1 = createBranch(1, 0, 0);
    tree.appendChild(level1);

    // Create branches for level 2
    for (var i = 0; i < 2; i++) {
        var angle = (i === 0) ? 30 : -30;
        var level2 = createBranch(2, angle, 2);
        level1.appendChild(level2);

        // Create branches for level 3
        for (var j = 0; j < 2; j++) {
            angle = (j === 0) ? 20 : -20;
            var level3 = createBranch(3, angle, 4);
            level2.appendChild(level3);
            
            // Create branches for level 4
            for (var k = 0; k < 2; k++) {
                angle = (k === 0) ? 20 : -20;
                var level4 = createBranch(4, angle, 5);
                level3.appendChild(level4);
            }
        }
    }
}

// Start the animation
growBranches();
