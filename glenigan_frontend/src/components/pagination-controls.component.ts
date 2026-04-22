/**
 * Pagination Controls Component
 */
class PaginationControlsController {
    public metadata!: any;
    public currentPage!: number;
    public loading!: boolean;
    public onGoToPage!: (params: { page: number }) => void;

    public getPageRange(): number[] {
        if (!this.metadata) return [];
        const pages: number[] = [];
        const maxVisible = 5;
        let start = Math.max(1, this.currentPage - 2);
        let end = Math.min(this.metadata.total_pages, start + maxVisible - 1);
        
        if (end - start < maxVisible - 1) {
            start = Math.max(1, end - maxVisible + 1);
        }

        for (let i = start; i <= end; i++) {
            pages.push(i);
        }
        return pages;
    }
}

const paginationControls: ng.IComponentOptions = {
    bindings: {
        metadata: '<',
        currentPage: '<',
        loading: '<',
        onGoToPage: '&'
    },
    templateUrl: 'src/templates/pagination-controls.html',
    controller: PaginationControlsController
};

angular.module('gleniganApp').component('paginationControls', paginationControls);
