interface Project {
    project_name: string;
    project_start: string;
    project_end: string;
    company: string;
    description: string;
    project_value: number;
    area: string;
}

interface Filters {
    keyword: string;
    area: string;
}

interface PaginationMetadata {
    total_count: number;
    page: number;
    per_page: number;
    total_pages: number;
}

interface PaginatedResponse {
    items: Project[];
    metadata: PaginationMetadata;
}

/**
 * Main Application Orchestrator
 */
class ProjectController {
    public projects: Project[] = [];
    public metadata: PaginationMetadata | null = null;
    public filters: Filters = {
        keyword: '',
        area: ''
    };
    public loading: boolean = false;
    public page: number = 1;
    public perPage: number = 20;

    // Use default backend API base URL if not provided
    private API_BASE_URL: string = (window as any).API_BASE_URL || 'http://localhost:8000';

    static $inject = ['$http', '$timeout'];

    constructor(private $http: ng.IHttpService, private $timeout: ng.ITimeoutService) {
        this.loadProjects();
    }

    public onPerPageChange(): void {
        this.page = 1;
        this.loadProjects();
    }

    public loadProjects(): void {
        this.loading = true;

        let url = `${this.API_BASE_URL}/projects?page=${this.page}&per_page=${this.perPage}`;

        if (this.filters.keyword) {
            url += `&keyword=${encodeURIComponent(this.filters.keyword)}`;
        }
        if (this.filters.area) {
            url += `&area=${encodeURIComponent(this.filters.area)}`;
        }

        this.$http.get<PaginatedResponse>(url)
            .then((response) => {
                this.projects = response.data.items;
                this.metadata = response.data.metadata;
            })
            .catch((error) => {
                console.error('Error fetching projects:', error);
                alert('Failed to load projects. Please ensure the backend is running.');
            })
            .finally(() => {
                this.loading = false;
            });
    }

    private filterTimeout: ng.IPromise<any> | null = null;
    public onFilterChange(): void {
        this.page = 1; // Reset to first page on filter change

        if (this.filterTimeout) {
            this.$timeout.cancel(this.filterTimeout);
        }
        this.filterTimeout = this.$timeout(() => {
            this.loadProjects();
        }, 300);
    }

    public resetFilters(): void {
        this.filters = { keyword: '', area: '' };
        this.page = 1;
        this.loadProjects();
    }

    public goToPage(p: number): void {
        this.page = p;
        this.loadProjects();
    }
}

// Bootstrap main module
angular.module('gleniganApp', [])
    .controller('ProjectController', ProjectController);
