{% extends "layouts/base.html" %}

{% block title %} Dashboard {% endblock %} 

<!-- Specific Page CSS goes HERE  -->
{% block stylesheets %}{% endblock stylesheets %}

{% block content %}

    <div class="content">
        <div class="row">
            <div class="col-12">
                <div class="card card-chart">
                    <div class="card-header ">
                        <div class="row">
                            <div class="col-sm-6 text-left">
                                <h5 class="card-category">Daily Meter Readings</h5>
                                <h2 class="card-title">Performance</h2>
                            </div>
                            <div class="col-sm-6">
                                <div class="btn-group btn-group-toggle float-right" data-toggle="buttons">
                                    <label class="btn btn-sm btn-primary btn-simple active" id="0">
                                        <input type="radio" name="options" checked>
                                        <span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">7 Days</span>
                                        <span class="d-block d-sm-none">
											<i class="tim-icons icon-single-02"></i>
										</span>
                                    </label>
                                    <label class="btn btn-sm btn-primary btn-simple" id="1">
                                        <input type="radio" class="d-none d-sm-none" name="options">
                                        <span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">14 Days</span>
                                        <span class="d-block d-sm-none">
											<i class="tim-icons icon-gift-2"></i>
										</span>
                                    </label>
                                    <label class="btn btn-sm btn-primary btn-simple" id="2">
                                        <input type="radio" class="d-none" name="options">
                                        <span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">30 days</span>
                                        <span class="d-block d-sm-none">
											<i class="tim-icons icon-tap-02"></i>
										</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="chart-area">
                            <canvas id="chartBig1"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-4">
                <div class="card card-chart">
                    <div class="card-header">
                        <h5 class="card-category">Online Meters</h5>
                        <h3 id="onlineMetersHeading" class="card-title"><i class="tim-icons icon-wifi text-success"></i>0</h3>
                    </div>
                    <div class="card-body">
                        <div class="chart-area">
                            <canvas id="chartLinePurple"></canvas>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="card card-chart">
                    <div class="card-header">
                        <h5 class="card-category">Meter Assets</h5>
                        <h3 id="meterAssetsHeading" class="card-title"><i class="tim-icons icon-delivery-fast text-info"></i> 0</h3>
                    </div>
                    <div class="card-body">
                        <div class="chart-area">
                            <canvas id="CountryChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="card card-chart">
                    <div class="card-header">
                        <h5 class="card-category">Meter Signal Level</h5>
                        <h3 id="meterSignalLevelHeading" class="card-title"><i class="tim-icons icon-wifi text-success"></i>0</h3>
                    </div>
                    <div class="card-body">
                        <div class="chart-area">
                            <canvas id="chartLineGreen"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </div>
		

		<div class="row">
			<div class="col-lg-6 col-md-12">
				<div class="card card-chart">
					<div class="card-header">
						<div class="row">
							<div class="col-sm-6 text-left">
								<h4 class="card-category">Daily Meter Readings - Distribution Division 1</h4>
								<h4 class="card-title">Performance</h4>
							</div>
							<div class="col-sm-6">
								<div class="btn-group btn-group-toggle float-right" data-toggle="buttons">
									<label class="btn btn-sm btn-primary btn-simple active" id="dd1-7days">
										<input type="radio" name="options-dd1" checked>
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">7 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-single-02"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd1-14days">
										<input type="radio" class="d-none d-sm-none" name="options-dd1">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">14 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-gift-2"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd1-30days">
										<input type="radio" class="d-none" name="options-dd1">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">30 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-tap-02"></i>
										</span>
									</label>
								</div>
							</div>
						</div>
					</div>
					<div class="card-body">
						<div class="chart-area">
							<canvas id="chartDD1"></canvas>
						</div>
					</div>
				</div>
			</div>
			<div class="col-lg-6 col-md-12">
				<div class="card card-chart">
					<div class="card-header">
						<div class="row">
							<div class="col-sm-6 text-left">
								<h4 class="card-category">Daily Meter Readings - Distribution Division 2</h4>
								<h4 class="card-title">Performance</h4>
							</div>
							<div class="col-sm-6">
								<div class="btn-group btn-group-toggle float-right" data-toggle="buttons">
									<label class="btn btn-sm btn-primary btn-simple active" id="dd2-7days">
										<input type="radio" name="options-dd2" checked>
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">7 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-single-02"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd2-14days">
										<input type="radio" class="d-none d-sm-none" name="options-dd2">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">14 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-gift-2"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd2-30days">
										<input type="radio" class="d-none" name="options-dd2">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">30 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-tap-02"></i>
										</span>
									</label>
								</div>
							</div>
						</div>
					</div>
					<div class="card-body">
						<div class="chart-area">
							<canvas id="chartDD2"></canvas>
						</div>
					</div>
				</div>
			</div>
		</div>


		<div class="row">
			<div class="col-lg-6 col-md-12">
				<div class="card card-chart">
					<div class="card-header">
						<div class="row">
							<div class="col-sm-6 text-left">
								<h4 class="card-category">Daily Meter Readings - Distribution Division 3</h4>
								<h4 class="card-title">Performance</h4>
							</div>
							<div class="col-sm-6">
								<div class="btn-group btn-group-toggle float-right" data-toggle="buttons">
									<label class="btn btn-sm btn-primary btn-simple active" id="dd3-7days">
										<input type="radio" name="options-dd3" checked>
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">7 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-single-02"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd3-14days">
										<input type="radio" class="d-none d-sm-none" name="options-dd3">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">14 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-gift-2"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd3-30days">
										<input type="radio" class="d-none" name="options-dd3">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">30 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-tap-02"></i>
										</span>
									</label>
								</div>
							</div>
						</div>
					</div>
					<div class="card-body">
						<div class="chart-area">
							<canvas id="chartDD3"></canvas>
						</div>
					</div>
				</div>
			</div>
		
			<div class="col-lg-6 col-md-12">
				<div class="card card-chart">
					<div class="card-header">
						<div class="row">
							<div class="col-sm-6 text-left">
								<h4 class="card-category">Daily Meter Readings - Distribution Division 4</h4>
								<h4 class="card-title">Performance</h4>
							</div>
							<div class="col-sm-6">
								<div class="btn-group btn-group-toggle float-right" data-toggle="buttons">
									<label class="btn btn-sm btn-primary btn-simple active" id="dd4-7days">
										<input type="radio" name="options-dd4" checked>
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">7 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-single-02"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd4-14days">
										<input type="radio" class="d-none d-sm-none" name="options-dd4">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">14 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-gift-2"></i>
										</span>
									</label>
									<label class="btn btn-sm btn-primary btn-simple" id="dd4-30days">
										<input type="radio" class="d-none" name="options-dd4">
										<span class="d-none d-sm-block d-md-block d-lg-block d-xl-block">30 Days</span>
										<span class="d-block d-sm-none">
											<i class="tim-icons icon-tap-02"></i>
										</span>
									</label>
								</div>
							</div>
						</div>
					</div>
					<div class="card-body">
						<div class="chart-area">
							<canvas id="chartDD4"></canvas>
						</div>
					</div>
				</div>
			</div>
		

		</div>
		





	
        <div class="row hidden_element" >
            <div class="col-lg-6 col-md-12">
				<div class="card card-tasks">
					<div class="card-header">
						<h6 class="title d-inline">Tasks (5)</h6>
						<p class="card-category d-inline">Today</p>
						<div class="dropdown">
							<button type="button" class="btn btn-link dropdown-toggle btn-icon" data-toggle="dropdown">
								<i class="tim-icons icon-settings-gear-63"></i>
							</button>
							<div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuLink">
								<a class="dropdown-item" href="#pablo">Action</a>
								<a class="dropdown-item" href="#pablo">Another action</a>
								<a class="dropdown-item" href="#pablo">Something else</a>
							</div>
						</div>
					</div>
					<div class="card-body">
						<div class="table-full-width table-responsive">
							<table class="table">
								<tbody>
								<tr>
									<td>
										<div class="form-check">
											<label class="form-check-label">
												<input class="form-check-input" type="checkbox" value="">
												<span class="form-check-sign">
													<span class="check"></span>
												</span>
											</label>
										</div>
									</td>
									<td>
										<p class="title">Review Smart Meter Data</p>
										<p class="text-muted">Check the daily data logs from smart meters for discrepancies.</p>
									</td>
									<td class="td-actions text-right">
										<button type="button" rel="tooltip" title="Edit Task" class="btn btn-link">
											<i class="tim-icons icon-pencil"></i>
										</button>
									</td>
								</tr>
								<tr>
									<td>
										<div class="form-check">
											<label class="form-check-label">
												<input class="form-check-input" type="checkbox" value="" checked="">
												<span class="form-check-sign">
													<span class="check"></span>
												</span>
											</label>
										</div>
									</td>
									<td>
										<p class="title">Verify Meter Installations</p>
										<p class="text-muted">Ensure all newly installed smart meters are functioning correctly.</p>
									</td>
									<td class="td-actions text-right">
										<button type="button" rel="tooltip" title="Edit Task" class="btn btn-link">
											<i class="tim-icons icon-pencil"></i>
										</button>
									</td>
								</tr>
								<tr>
									<td>
										<div class="form-check">
											<label class="form-check-label">
												<input class="form-check-input" type="checkbox" value="">
												<span class="form-check-sign">
													<span class="check"></span>
												</span>
											</label>
										</div>
									</td>
									<td>
										<p class="title">Update Meter Firmware</p>
										<p class="text-muted">Apply the latest firmware updates to smart meters to improve performance.</p>
									</td>
									<td class="td-actions text-right">
										<button type="button" rel="tooltip" title="Edit Task" class="btn btn-link">
											<i class="tim-icons icon-pencil"></i>
										</button>
									</td>
								</tr>
								<tr>
									<td>
										<div class="form-check">
											<label class="form-check-label">
												<input class="form-check-input" type="checkbox" value="">
												<span class="form-check-sign">
													<span class="check"></span>
												</span>
											</label>
										</div>
									</td>
									<td>
										<p class="title">Monitor Energy Consumption</p>
										<p class="text-muted">Track and analyze energy consumption data from smart meters.</p>
									</td>
									<td class="td-actions text-right">
										<button type="button" rel="tooltip" title="Edit Task" class="btn btn-link">
											<i class="tim-icons icon-pencil"></i>
										</button>
									</td>
								</tr>
								<tr>
									<td>
										<div class="form-check">
											<label class="form-check-label">
												<input class="form-check-input" type="checkbox" value="">
												<span class="form-check-sign">
													<span class="check"></span>
												</span>
											</label>
										</div>
									</td>
									<td>
										<p class="title">Generate Usage Reports</p>
										<p class="text-muted">Prepare and distribute reports on electricity usage and meter performance.</p>
									</td>
									<td class="td-actions text-right">
										<button type="button" rel="tooltip" title="Edit Task" class="btn btn-link">
											<i class="tim-icons icon-pencil"></i>
										</button>
									</td>
								</tr>
								<tr>
									<td>
										<div class="form-check">
											<label class="form-check-label">
												<input class="form-check-input" type="checkbox" value="">
												<span class="form-check-sign">
													<span class="check"></span>
												</span>
											</label>
										</div>
									</td>
									<td>
										<p class="title">Inspect Meter Accuracy</p>
										<p class="text-muted">Perform accuracy checks on smart meters to ensure proper measurement.</p>
									</td>
									<td class="td-actions text-right">
										<button type="button" rel="tooltip" title="Edit Task" class="btn btn-link">
											<i class="tim-icons icon-pencil"></i>
										</button>
									</td>
								</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>

			
			
			
			
			
			<div class="col-lg-6 col-md-12">
				<div class="card">
					<div class="card-header">
						<h4 class="card-title">Smart Electricity Metering Data</h4>
					</div>
					<div class="card-body">
						<div class="table-responsive">
							<table class="table tablesorter" id="">
								<thead class="text-primary">
								<tr>
									<th>
										Meter ID
									</th>
									<th>
										Location
									</th>
									<th>
										Installation Date
									</th>
									<th class="text-center">
										Monthly Consumption (kWh)
									</th>
								</tr>
								</thead>
								<tbody>
								<tr>
									<td>
										MTR-001
									</td>
									<td>
										123 Elm Street, Springfield
									</td>
									<td>
										2022-01-15
									</td>
									<td class="text-center">
										450
									</td>
								</tr>
								<tr>
									<td>
										MTR-002
									</td>
									<td>
										456 Oak Avenue, Springfield
									</td>
									<td>
										2022-03-10
									</td>
									<td class="text-center">
										520
									</td>
								</tr>
								<tr>
									<td>
										MTR-003
									</td>
									<td>
										789 Pine Road, Springfield
									</td>
									<td>
										2022-05-22
									</td>
									<td class="text-center">
										610
									</td>
								</tr>
								<tr>
									<td>
										MTR-004
									</td>
									<td>
										101 Maple Drive, Springfield
									</td>
									<td>
										2022-07-08
									</td>
									<td class="text-center">
										470
									</td>
								</tr>
								<tr>
									<td>
										MTR-005
									</td>
									<td>
										202 Birch Lane, Springfield
									</td>
									<td>
										2022-09-12
									</td>
									<td class="text-center">
										540
									</td>
								</tr>
								<tr>
									<td>
										MTR-006
									</td>
									<td>
										303 Cedar Street, Springfield
									</td>
									<td>
										2022-11-05
									</td>
									<td class="text-center">
										630
									</td>
								</tr>
								<tr>
									<td>
										MTR-007
									</td>
									<td>
										404 Willow Road, Springfield
									</td>
									<td>
										2023-01-19
									</td>
									<td class="text-center">
										500
									</td>
								</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>

			
			
			
			
			
        </div>
    </div>

{% endblock content %}

<!-- Specific Page JS goes HERE  -->
{% block javascripts %}
<script src="{{ url_for('static', filename='assets/demo/moment.js') }}"></script>
<script src="{{ url_for('static', filename='assets/demo/demo.js') }}"></script>
<script src="{{ url_for('static', filename='assets/demo/dash_DD_charts.js') }}"></script>

<script>
    $(document).ready(function () {

        demo.initDashboardPageCharts();
		demo.updateDashboardPageCharts();
		demo.loadDailyOnlineMeterCount();
		demo.loadAssetSummery();
        $("#0").trigger("click");
		
    });
</script>

{% endblock javascripts %}
