import React from 'react';

// PUBLIC_INTERFACE
export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="filter-title">Filters</div>
      <div className="placeholder-filters">
        {/* Placeholder for filter controls – coming soon */}
        - Cuisine<br />
        - Prep Time<br />
        - Dietary<br />
        - Favorites<br />
      </div>
    </aside>
  );
}
