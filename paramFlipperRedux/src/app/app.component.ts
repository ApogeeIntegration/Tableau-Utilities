import { AfterViewInit, Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { DataSource } from '@tableau/extensions-api-types';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements AfterViewInit {
  public title = 'Param Flipper';
  public currentlyPlaying = false;
  public params = ['Test', 'Test2', 'Test3'];
  public paramValues = ['Test', 'Test2', 'Test3'];
  public currentParamName = 'Test';
  public currentParamValue = 'Test';

  public paramForm = new FormGroup({
    parameter: new FormControl(this.currentParamName, [Validators.required]),
    flipDuration: new FormControl(2.0, [Validators.required, Validators.min(0)]),
    stepSize: new FormControl('', [Validators.required, Validators.min(0)]),
    minVal: new FormControl('', [Validators.required]),
    maxVal: new FormControl('', [Validators.required]),
    loop: new FormControl(false)
  });

  public async ngAfterViewInit() {
    await tableau.extensions.initializeAsync();
  }

  public async findParameter(paramName: string) {
    const params = await tableau.extensions.dashboardContent?.dashboard.getParametersAsync();

    return params?.find((x) => x.name === paramName);
  }

  public startStopPlayback() {
    this.currentlyPlaying = !this.currentlyPlaying;
  }

  public updateCurrentParam(event: any) {
    this.currentParamName = event.target.value;
  }

  private async getParameters() {
    return await tableau.extensions.dashboardContent?.dashboard.getParametersAsync();
  }
}
