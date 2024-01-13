function createBranch(parent, level, angle, length, delay) {
    console.log(`Maturity phase ${level} entered`);
    // Create a new branch element
    var branch = document.createElement('div');
    branch.className = 'branch';
    branch.style.width = '2px';
    branch.style.height = '0';
    branch.style.background = '#654321';
    branch.style.position = 'absolute';
    branch.style.bottom = '0';
    branch.style.left = '50%';
    branch.style.transformOrigin = 'bottom';
    branch.style.transform = `translateX(-50%) rotate(${angle}deg)`;
    parent.appendChild(branch);

    // Animate the branch
    branch.animate([
        { height: '0', bottom: '0' },
        { height: `${length}px`, bottom: `${length}px` }
    ], {
        duration: 1000,
        delay: delay,
        fill: 'forwards'
    });

    // If we haven't reached the last level, create two more branches
    if (level < 3) {
        setTimeout(() => {
            createBranch(branch, level + 1, 20, length / 2, 0);
            createBranch(branch, level + 1, -20, length / 2, 0);
        }, delay + 1000); // Wait for the current branch to finish growing
    }
}

console.log("Tree planted");
// Start growing branches from the trunk
var trunk = document.getElementById('tree');
trunk.style.height = '150px'; // Set trunk height
createBranch(trunk, 1, 0, 150, 0); // Create the first branch
