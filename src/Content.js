import profile from './IMG_2999.JPG';
import springboot_icon from './springboot.png';
import aws_icon from './aws.png';
import kubernetes_icon from './kubernetes.png'

export default function Content() {
    return <div className="content">
        <div className="container pad-1 span-2">
            <p className="user-caption">Hey, I'm Dhruv, A backend developer with expertise in AWS Services.</p>
            <div className="flex-container">
                <figure className="skill-figure">
                    <img src={springboot_icon} alt="Spring boot icon" />
                    <figcaption>Sping Boot</figcaption>
                </figure>
                <figure className="skill-figure">
                    <img src={kubernetes_icon} alt="Kubernetes icon" />
                    <figcaption>Kubernetes</figcaption>
                </figure>
                <figure className="skill-figure">
                    <img src={aws_icon} alt="AWS icon" />
                    <figcaption>AWS</figcaption>
                </figure>
            </div>
        </div>
        <img className="user-image" src={profile} alt="Profile" />
    </div>
}