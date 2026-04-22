describe('Glenigan App', function() {
    beforeEach(module('gleniganApp'));

    describe('ProjectController', function() {
        var $controller, $httpBackend, $timeout, ctrl;

        beforeEach(inject(function(_$controller_, _$httpBackend_, _$timeout_) {
            $controller = _$controller_;
            $httpBackend = _$httpBackend_;
            $timeout = _$timeout_;
            
            // Mock initial load
            $httpBackend.expectGET('http://0.0.0.0:8000/projects?page=1&per_page=20')
                .respond({ items: [], metadata: { total_count: 0, total_pages: 0 } });
            
            ctrl = $controller('ProjectController');
        }));

        it('should initialize with default values', function() {
            expect(ctrl.page).toBe(1);
            expect(ctrl.perPage).toBe(20);
            expect(ctrl.loading).toBe(true);
        });

        it('should load projects and set metadata', function() {
            $httpBackend.flush();
            expect(ctrl.loading).toBe(false);
            expect(ctrl.metadata.total_count).toBe(0);
        });

        it('should handle search with debounce', function() {
            $httpBackend.flush();
            ctrl.filters.keyword = 'Stadium';
            ctrl.onFilterChange();
            
            // Should not call immediately
            expect(ctrl.page).toBe(1);
            
            // Set up expectation before flushing timeout
            $httpBackend.expectGET('http://0.0.0.0:8000/projects?page=1&per_page=20&keyword=Stadium')
                .respond({ items: [], metadata: { total_count: 0 } });

            // Fast forward time
            $timeout.flush();
            
            $httpBackend.flush();
        });


        it('should reset filters', function() {
            $httpBackend.flush();
            ctrl.filters.keyword = 'Stadium';
            ctrl.resetFilters();
            
            expect(ctrl.filters.keyword).toBe('');
            $httpBackend.expectGET('http://0.0.0.0:8000/projects?page=1&per_page=20')
                .respond({ items: [], metadata: { total_count: 0 } });
            $httpBackend.flush();
        });
    });

    describe('Components', function() {
        var $componentController;

        beforeEach(inject(function(_$componentController_) {
            $componentController = _$componentController_;
        }));

        it('resultsHeader should calculate end index correctly', function() {
            var bindings = { totalCount: 100, currentPage: 1, perPage: 20 };
            var ctrl = $componentController('resultsHeader', null, bindings);
            expect(ctrl.getEndIndex()).toBe(20);

            ctrl.currentPage = 5;
            expect(ctrl.getEndIndex()).toBe(100);

            ctrl.currentPage = 6; // Out of bounds
            expect(ctrl.getEndIndex()).toBe(100);
        });

        it('paginationControls should calculate page range correctly', function() {
            var bindings = { 
                metadata: { total_pages: 10 }, 
                currentPage: 1 
            };
            var ctrl = $componentController('paginationControls', null, bindings);
            var range = ctrl.getPageRange();
            expect(range).toEqual([1, 2, 3, 4, 5]);

            ctrl.currentPage = 10;
            range = ctrl.getPageRange();
            expect(range).toEqual([6, 7, 8, 9, 10]);
        });
    });
});
